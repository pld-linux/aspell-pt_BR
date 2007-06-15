Summary:	Portuguese dictionaries for aspell
Summary(pl.UTF-8):	Portugalskie słowniki dla aspella
Summary(pt_BR.UTF-8):	Dicionário de português para o aspell
Name:		aspell-pt_BR
Version:	20070411
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/pt_BR/aspell6-pt_BR-%{version}-0.tar.bz2
# Source0-md5:	31f537cb1da39229f7545f4766bd7185
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60.0
Requires:	aspell >= 3:0.60.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Portuguese dictionaries (i.e. word lists) for aspell.

%description -l pl.UTF-8
Portugalskie słowniki (listy słów) dla aspella.

%description -l pt_BR.UTF-8
Dicionários da língua portuguesa para o verificador ortográfico
aspell.

%prep
%setup -q -n aspell6-pt_BR-%{version}-0

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
%doc Copyright README doc/README.Aspell doc/colaboradores.txt
%lang(pt_BR) %doc doc/LEIAME.Aspell
%{_libdir}/aspell/*
%{_datadir}/aspell/*
