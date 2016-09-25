require 'spec_helper'

set :os, family: 'redhat', release: '7', arch: 'x86_64'

describe package('{{ cookiecutter.role_name }}') do
  it { should be_installed }
end
