#!/usr/bin/env ruby
# regex that matchs school
puts ARGV[0].match(/School/i)[0] if ARGV[0].match(/School/i)
