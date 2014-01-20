#!/usr/bin/env ruby

require 'psd'

PSD.open(ARGV[0]) do |psd|
  p psd.tree.to_hash
end
