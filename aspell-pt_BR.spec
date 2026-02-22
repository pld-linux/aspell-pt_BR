Summary:	Portuguese dictionaries for aspell
Summary(pl.UTF-8):	Portugalskie słowniki dla aspella
Summary(pt_BR.UTF-8):	Dicionário de português para o aspell
Name:		aspell-pt_BR
Version:	20131030
Release:	3
%define	subv	12-0
License:	LGPL v2.1+
Group:		Applications/Text
Source0:	https://ftp.gnu.org/gnu/aspell/dict/pt_BR/aspell6-pt_BR-%{version}-%{subv}.tar.bz2
# Source0-md5:	9ac547609aeaa3891dfa00407b7ffb83
URL:		http://aspell.net/
BuildRequires:	aspell >= 3:0.60.0
BuildRequires:	which
Requires:	aspell >= 3:0.60.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Portuguese dictionaries (i.e. word lists) for aspell.

%description -l pl.UTF-8
Portugalskie słowniki (listy słów) dla aspella.

%description -l pt_BR.UTF-8
Dicionários da língua portuguesa para o verificador ortográfico
aspell.

%prep
%setup -q -n aspell6-pt_BR-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_prefix}/lib/aspell/pt_BR.multi
%{_prefix}/lib/aspell/pt_BR.rws
%{_prefix}/lib/aspell/brasileiro.alias
%{_prefix}/lib/aspell/brazilian.alias
%{_datadir}/aspell/br-abnt2.kbd
%{_datadir}/aspell/pt_BR.dat
%{_datadir}/aspell/pt_BR_affix.dat
