# Define the target output file
OUTPUT_FILE = output.txt

# Get the list of all CSV files in the causal_datasets directory
CAUS_FILES = $(wildcard causal_datasets/*.csv)

# Rule to ensure the output directory exists
var/out/smos:
	mkdir -p var/out/smos

# Rule to process all files and save the output into a single file
$(OUTPUT_FILE): $(CAUS_FILES) 
	@echo "Processing all files into $@"
	@> $@ # Clear the file if it exists
	@for file in $(CAUS_FILES); do \
		echo "Processing $$file" >> $@; \
		python3 ./causal_test.py --causal_dataset $$file >> $@; \
		echo "===================" >> $@; \
	done

# Target to trigger the processing
demo: $(OUTPUT_FILE)

# Clean target to remove the output file and directory
clean:
	rm -rf output.txt
