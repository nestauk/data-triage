#!/usr/bin/env bash

# Check only one arg
if (( $# != 1 ))
then
  echo -e "Usage:\n\n\tbash start-triage.sh <DATASET_NAME>\n\n(No spaces, obviously)"
  exit 1
fi

# Check running from root directory
if [[ "${PWD##*/}" != "data-triage" ]];
then
    echo -e "You must run this script from the `data-triage` directory."
    exit 1
fi

NEW_DIR="datasets/${1}"

# Check dir doesn't exist
if [[ -d "${NEW_DIR}" ]]; then
    echo -e "\nError:\n\t${NEW_DIR} already exists.\n"
    exit 1
fi


# Check jupyter is installed
if ! [ -x "$(command -v jupyter)" ]; then
    echo -e "\nError:\n\tYou must install jupyter before continuing.\n"
    exit 1
fi

cp -r datasets/.template ${NEW_DIR}
sed -i -e "s/{{template}}/${1}/g" ${NEW_DIR}/*/*ipynb
sed -i -e "s/{{template}}/${1}/g" ${NEW_DIR}/README.md
jupyter trust ${NEW_DIR}/*/*ipynb &> /dev/null
rm ${NEW_DIR}/*/*ipynb-e

echo -e "\nNew data triage directory created at\n\t${NEW_DIR}\n"
