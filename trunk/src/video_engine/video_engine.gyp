# Copyright (c) 2011 The WebRTC project authors. All Rights Reserved.
#
# Use of this source code is governed by a BSD-style license
# that can be found in the LICENSE file in the root of the source
# tree. An additional intellectual property rights grant can be found
# in the file PATENTS.  All contributing project authors may
# be found in the AUTHORS file in the root of the source tree.

{
  'includes': [
    '../common_settings.gypi', # Common settings
    'main/source/video_engine_core.gypi',
  ],

  # Test targets, excluded when building with chromium.
  'conditions': [
    ['build_with_chromium==0', {
      'includes': [
        'main/test/AutoTest/vie_auto_test.gypi',
        'main/test/WindowsTest/windowstest.gypi',
      ], # includes
    }], # build_with_chromium
  ], # conditions   
}

