#
# The include should be a single file that contains:
# export USER := {user}
# export PASSWORD := {password}
#
include env

$(info $$KEY is [${API_KEY}])

all:
	python3 main.py

.PHONY: all