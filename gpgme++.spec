%define major 7
%define libname %mklibname gpgme++
%define devname %mklibname gpgme++ -d

Name:		gpgme++
Version:	2.0.0
Release:	1
Source0:	https://gnupg.org/ftp/gcrypt/gpgmepp/gpgmepp-%{version}.tar.xz
Summary:	C++ bindings to GPGme
URL:		https://github.com/gpgme++/gpgme++
License:	LGPL
Group:		System/Libraries
BuildRequires:	pkgconfig(gpgme)
BuildRequires:	cmake
BuildSystem:	cmake

%description
C++ bindings to GPGme

%package -n %{libname}
Summary:	C++ bindings to GPGme
Group:		System/Libraries
%rename %{mklibname gpgmepp 6}
%ifarch %{x86_64} %{aarch64} %{riscv64}
Provides:	libgpgmepp.so.6()(64bit)
%else
Provides:	libgpgmepp.so.6()
%endif

%description -n %{libname}
C++ bindings to GPGme

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}:
C++ bindings to GPGme

%install -a
# No significant ABI changes, (almost?) everything should
# keep working with the compat symlink.
ln -s libgpgmepp.so.%{major} %{buildroot}%{_libdir}/libgpgmepp.so.6

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/*.so.6

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*
