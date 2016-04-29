#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-typhoeus
Version  : 1.0.1
Release  : 7
URL      : https://rubygems.org/downloads/typhoeus-1.0.1.gem
Source0  : https://rubygems.org/downloads/typhoeus-1.0.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-ethon
BuildRequires : rubygem-faraday
BuildRequires : rubygem-ffi
BuildRequires : rubygem-guard-rspec
BuildRequires : rubygem-multipart-post
BuildRequires : rubygem-rack
BuildRequires : rubygem-rack-protection
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-sinatra
BuildRequires : rubygem-tilt

%description
# Typhoeus [![Build Status](https://img.shields.io/travis/typhoeus/typhoeus/master.svg)](https://travis-ci.org/typhoeus/typhoeus) [![Code Climate](https://img.shields.io/codeclimate/github/typhoeus/typhoeus.svg)](https://codeclimate.com/github/typhoeus/typhoeus) [![Gem Version](https://img.shields.io/gem/v/typhoeus.svg)](https://rubygems.org/gems/typhoeus)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n typhoeus-1.0.1
gem spec %{SOURCE0} -l --ruby > rubygem-typhoeus.gemspec

%build
gem build rubygem-typhoeus.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
typhoeus-1.0.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/typhoeus-0.7.2 && sed -i -e '/require "bundler"/ s/^/#/' -e '/Bundler\.setup/ s/^/#/' spec/spec_helper.rb && rspec -I.:lib spec/ && popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/typhoeus-1.0.1.gem
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/.rspec
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/CHANGELOG.md
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/CONTRIBUTING.md
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/Guardfile
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/README.md
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/UPGRADE.md
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/rack/typhoeus.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/rack/typhoeus/middleware/params_decoder.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/rack/typhoeus/middleware/params_decoder/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/adapters/faraday.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/config.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/easy_factory.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/errors.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/errors/no_stub.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/errors/typhoeus_error.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/expectation.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/hydra.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/hydra/addable.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/hydra/before.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/hydra/block_connection.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/hydra/cacheable.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/hydra/memoizable.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/hydra/queueable.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/hydra/runnable.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/hydra/stubbable.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/pool.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/railtie.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/request.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/request/actions.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/request/before.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/request/block_connection.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/request/cacheable.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/request/callbacks.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/request/marshal.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/request/memoizable.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/request/operations.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/request/responseable.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/request/streamable.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/request/stubbable.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/response.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/response/cacheable.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/response/header.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/response/informations.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/response/status.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/lib/typhoeus/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/perf/profile.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/perf/vs_nethttp.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/rack/typhoeus/middleware/params_decoder/helper_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/rack/typhoeus/middleware/params_decoder_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/support/localhost_server.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/support/memory_cache.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/support/server.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/adapters/faraday_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/config_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/easy_factory_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/errors/no_stub_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/expectation_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/hydra/addable_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/hydra/before_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/hydra/block_connection_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/hydra/cacheable_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/hydra/memoizable_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/hydra/queueable_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/hydra/runnable_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/hydra/stubbable_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/hydra_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/pool_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/request/actions_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/request/before_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/request/block_connection_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/request/cacheable_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/request/callbacks_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/request/marshal_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/request/memoizable_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/request/operations_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/request/responseable_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/request/stubbable_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/request_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/response/header_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/response/informations_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/response/status_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus/response_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/spec/typhoeus_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/typhoeus-1.0.1/typhoeus.gemspec
/usr/lib64/ruby/gems/2.3.0/specifications/typhoeus-1.0.1.gemspec
