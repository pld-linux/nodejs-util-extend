%define		pkg	util-extend
Summary:	Node's internal object extension function
Name:		nodejs-%{pkg}
Version:	1.0.1
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/util-extend/-/%{pkg}-%{version}.tgz
# Source0-md5:	e14ca0f0df2bc5a1c7f06d1fb874e7a6
URL:		https://github.com/isaacs/util-extend
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Node object extending function that Node uses for Node!

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -p extend.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
