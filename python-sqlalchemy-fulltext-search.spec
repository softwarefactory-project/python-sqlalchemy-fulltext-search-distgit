%global sum     Fulltext search support with MySQL & SQLAlchemy

Name:           python-sqlalchemy-fulltext-search
Version:        0.2.3
Release:        1%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/mengzhuo/sqlalchemy-fulltext-search
Source0:        https://github.com/mengzhuo/sqlalchemy-fulltext-search/archive/%{version}.tar.gz

BuildArch:      noarch


%description
%{sum}


%package -n python2-sqlalchemy-fulltext-search
Summary:        %{sum}

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

Requires:       python-sqlalchemy


%description -n python2-sqlalchemy-fulltext-search
%{sum}


%prep
%autosetup -n sqlalchemy-fulltext-search-%{version}


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}


%files
%doc CHANGES.rst
%license LICENSE


%files -n python2-sqlalchemy-fulltext-search
%{python2_sitelib}/SQLAlchemy_FullText_Search*.egg-info
%{python2_sitelib}/sqlalchemy_fulltext


%changelog
* Tue Mar 14 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 0.2.3-1
- Initial packaging
