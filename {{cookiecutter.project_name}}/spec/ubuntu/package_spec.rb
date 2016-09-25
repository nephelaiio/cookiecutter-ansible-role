require 'spec_helper'

set :os, family: 'ubuntu', release: 'xenial', arch: 'x86_64'

describe package('{{ cookiecutter.role_name }}') do
  it { should be_installed }
end
