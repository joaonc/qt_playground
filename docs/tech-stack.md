Python packages and other technologies used throughout this project.

#### Semantic versioning
`semantic-version`:
[https://github.com/rbarrois/python-semanticversion](https://github.com/rbarrois/python-semanticversion)

#### YAML
`pyyaml`: [https://pyyaml.org](https://pyyaml.org/)

While this package is not included in the Python distribution, it's pretty standard when dealing
with YAML files.

In this project, there are three main reasons YAML is used instead of JSON:

* Comments.  
  YAML files can have comments, which can be very useful.
  ```yaml
  # Comment on a YAML file
  some_value: True  # Inline comments also supported
  ```
* Multiline.  
  YAML allows for multiline entries.
  ```yaml
  key_1: >
    This is a simple line.
    This multiline text will
    transform into a single line.
  key_2: |
    This is a simple line.
    This text will retain
    its original newlines.
  ```
* Legibility.  
  YAML is usually less verbose than JSON, making it more readable.
