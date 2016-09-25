require 'spec_helper'

describe package('{{ cookiecutter.role_name }}') do
  it { should be_installed }
end
