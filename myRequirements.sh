set -e

env_dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

source /home/maojingwei/project/common_tools_for_centos/myhead.sh pyenv $env_dir

if [ "$1" != "run" ]; then
    echo "start installing requirements"
fi
