# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Classes for dsub job script and resource."""

import collections

DEFAULT_MIN_CORES = 1
DEFAULT_MIN_RAM = 3.75
DEFAULT_DISK_SIZE = 200
DEFAULT_BOOT_DISK_SIZE = 10
DEFAULT_SCOPES = [
    'https://www.googleapis.com/auth/bigquery',
]


class JobResources(
    collections.namedtuple('JobResources', [
        'min_cores', 'min_ram', 'disk_size', 'boot_disk_size', 'preemptible',
        'image', 'logging', 'zones', 'scopes', 'keep_alive'
    ])):
  """Job resource parameters related to CPUs, memory, and disk.

  Attributes:
    min_cores (int): number of CPU cores
    min_ram (float): amount of memory (in GB)
    disk_size (int): size of the data disk (in GB)
    boot_disk_size (int): size of the boot disk (in GB)
    preemptible (bool): use a preemptible VM for the job
    image (str): Docker image name
    logging (param_util.LoggingParam): path to location for jobs to write logs
    zones (str): location in which to run the job
    scopes (list): OAuth2 scopes for the job
    keep_alive (int): Seconds to keep VM alive on failure
  """
  __slots__ = ()

  def __new__(cls,
              min_cores=DEFAULT_MIN_CORES,
              min_ram=DEFAULT_MIN_RAM,
              disk_size=DEFAULT_DISK_SIZE,
              boot_disk_size=DEFAULT_BOOT_DISK_SIZE,
              preemptible=False,
              image=None,
              logging=None,
              zones=None,
              scopes=DEFAULT_SCOPES,
              keep_alive=None):
    return super(JobResources, cls).__new__(cls, min_cores, min_ram, disk_size,
                                            boot_disk_size, preemptible, image,
                                            logging, zones, scopes, keep_alive)


class Script(object):
  """Script to be run by for the job.

  The Pipeline's API specifically supports bash commands as the docker
  command. To support any type of script (Python, Ruby, etc.), the contents
  are uploaded as a simple environment variable input parameter.
  The docker command then writes the variable contents to a file and
  executes it.

  Attributes:
    name: (str) File name of this script.
    value: (str) Content of this script.
  """

  def __init__(self, name, value):
    self.name = name
    self.value = value
