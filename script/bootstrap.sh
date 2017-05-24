#!/usr/bin/env bash
# -*- coding: utf-8 -*-

export PROJECT_NAME=python-example-graphene

export PYTHON_VERSION=3.6.1
export PYENV_NAME="${PROJECT_NAME}"

export GRIP_PORT=6430

export APP_IP=0.0.0.0
export APP_PORT=8000

# Vars Dir
export ROOT_DIR
ROOT_DIR=$(pwd)
export RESOURCES_DIR="$ROOT_DIR/resources"
export RESOURCES_DB_DIR="$RESOURCES_DIR/db"
export PROVISION_DIR="$ROOT_DIR/provision/ansible"
export SOURCE_DIR="${ROOT_DIR}/src/"
export REQUIREMENTS_DIR="${SOURCE_DIR}/requirements/"
