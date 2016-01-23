/* Copyright 2015 Google Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

#ifndef TENSORFLOW_EXAMPLES_LABEL_IMAGE_COMMAND_LINE_FLAGS_H
#define TENSORFLOW_EXAMPLES_LABEL_IMAGE_COMMAND_LINE_FLAGS_H

#include <vector>
#include "tensorflow/core/platform/types.h"

// This is a simple command-line argument parsing module to help us handle
// example parameters. The recommended way of using it is with local variables
// and an initializer list of Flag objects, for example:
//
// int some_int = 10;
// bool some_switch = false;
// string some_name = "something";
// bool parsed_values_ok = ParseFlags(&argc, argv, {
//   Flag("some_int", &some_int),
//   Flag("some_switch", &some_switch),
//   Flag("some_name", &some_name)});
//
// The argc and argv values are adjusted by the Parse function so all that
// remains is the program name (at argv[0]) and any unknown arguments fill the
// rest of the array. This means you can check for flags that weren't understood
// by seeing if argv is greater than 1.
// The result indicates if there were any errors parsing the values that were
// passed to the command-line switches. For example, --some_int=foo would return
// false because the argument is expected to be an integer.
class Flag {
 public:
  Flag(const char* name, tensorflow::int32* dst1);
  Flag(const char* name, bool* dst);
  Flag(const char* name, tensorflow::string* dst);

  bool Parse(tensorflow::string arg, bool* value_parsing_ok) const;

 private:
  tensorflow::string name_;
  enum { TYPE_INT, TYPE_BOOL, TYPE_STRING } type_;
  int* int_value_;
  bool* bool_value_;
  tensorflow::string* string_value_;
};

bool ParseFlags(int* argc, char** argv, const std::vector<Flag>& flag_list);

#endif  // TENSORFLOW_EXAMPLES_LABEL_IMAGE_COMMAND_LINE_FLAGS_H
