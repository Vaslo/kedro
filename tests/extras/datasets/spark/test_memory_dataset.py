# Copyright 2021 QuantumBlack Visual Analytics Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND
# NONINFRINGEMENT. IN NO EVENT WILL THE LICENSOR OR OTHER CONTRIBUTORS
# BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# The QuantumBlack Visual Analytics Limited ("QuantumBlack") name and logo
# (either separately or in combination, "QuantumBlack Trademarks") are
# trademarks of QuantumBlack. The License does not grant you any right or
# license to the QuantumBlack Trademarks. You may not use the QuantumBlack
# Trademarks or any confusingly similar mark as a trademark for your product,
# or use the QuantumBlack Trademarks in any other manner that might cause
# confusion in the marketplace, including but not limited to in advertising,
# on websites, or on software.
#
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest
from pyspark.sql import DataFrame as SparkDataFrame
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

from kedro.io import MemoryDataSet


def _update_spark_df(data, idx, jdx, value):
    session = SparkSession.builder.getOrCreate()
    data = session.createDataFrame(data.rdd.zipWithIndex()).select(
        col("_1.*"), col("_2").alias("__id")
    )
    cname = data.columns[idx]
    return data.withColumn(
        cname, when(col("__id") == jdx, value).otherwise(col(cname))
    ).drop("__id")


def _check_equals(data1, data2):
    if isinstance(data1, SparkDataFrame) and isinstance(data2, SparkDataFrame):
        return data1.toPandas().equals(data2.toPandas())
    return False  # pragma: no cover


@pytest.fixture
def spark_data_frame(spark_session):
    return spark_session.createDataFrame(
        [(1, 4, 5), (2, 5, 6)], ["col1", "col2", "col3"]
    )


@pytest.fixture
def memory_dataset(spark_data_frame):
    return MemoryDataSet(data=spark_data_frame)


def test_load_modify_original_data(memory_dataset, spark_data_frame):
    """Check that the data set object is not updated when the original
    SparkDataFrame is changed."""
    spark_data_frame = _update_spark_df(spark_data_frame, 1, 1, -5)
    assert not _check_equals(memory_dataset.load(), spark_data_frame)


def test_save_modify_original_data(spark_data_frame):
    """Check that the data set object is not updated when the original
    SparkDataFrame is changed."""
    memory_dataset = MemoryDataSet()
    memory_dataset.save(spark_data_frame)
    spark_data_frame = _update_spark_df(spark_data_frame, 1, 1, "new value")

    assert not _check_equals(memory_dataset.load(), spark_data_frame)


def test_load_returns_same_spark_object(memory_dataset, spark_data_frame):
    """Test that consecutive loads point to the same object in case of
    a SparkDataFrame"""
    loaded_data = memory_dataset.load()
    reloaded_data = memory_dataset.load()
    assert _check_equals(loaded_data, spark_data_frame)
    assert _check_equals(reloaded_data, spark_data_frame)
    assert loaded_data is reloaded_data


def test_str_representation(memory_dataset):
    """Test string representation of the data set"""
    assert "MemoryDataSet(data=<DataFrame>)" in str(memory_dataset)
