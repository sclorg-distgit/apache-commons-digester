%global pkg_name apache-commons-digester
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global base_name digester
%global short_name commons-%{base_name}

Name:          %{?scl_prefix}%{pkg_name}
Version:       1.8.1
Release:       19.10%{?dist}
Summary:       XML to Java object mapping module
License:       ASL 2.0
URL:           http://commons.apache.org/%{base_name}/

Source0:       http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz

BuildArch:     noarch

BuildRequires: %{?scl_prefix_java_common}javapackages-tools
BuildRequires: %{?scl_prefix}apache-commons-parent >= 26-7
BuildRequires: %{?scl_prefix_java_common}apache-commons-beanutils >= 1.8
BuildRequires: %{?scl_prefix_java_common}apache-commons-logging >= 1.1.1
BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: %{?scl_prefix}maven-antrun-plugin
BuildRequires: %{?scl_prefix}maven-assembly-plugin
BuildRequires: %{?scl_prefix}maven-resources-plugin
BuildRequires: %{?scl_prefix}maven-doxia-sitetools
BuildRequires: %{?scl_prefix}maven-plugin-bundle

%description
Many projects read XML configuration files to provide initialization of
various Java objects within the system. There are several ways of doing this,
and the Digester component was designed to provide a common implementation
that can be used in many different projects

%package javadoc
Summary:       API documentation for %{pkg_name}

%description javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x

sed -i 's/\r//' RELEASE-NOTES*.txt LICENSE.txt NOTICE.txt

%mvn_file : %{pkg_name} %{short_name}
%mvn_alias : %{short_name}:%{short_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES*

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.8.1-19.10
- Mass rebuild 2015-01-13

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.8.1-19.9
- Rebuild to regenerate requires

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.8.1-19.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.1-19.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.1-19.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.1-19.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.1-19.4
- Remove requires on java

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.1-19.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.1-19.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.1-19.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.8.1-19
- Mass rebuild 2013-12-27

* Fri Sep 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.1-18
- Add BuildRequires on apache-commons-parent >= 26-7

* Mon Aug 19 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.8.1-17
- Migrate away from mvn-rpmbuild (#997455)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.1-16
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.1-15
- Remove unneeded BR: maven-idea-plugin

* Mon Feb 18 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.8.1-14
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug  7 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.1-12
- Fix file permissions
- Install LICENSE and NOTICE with javadoc package

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 30 2011 Alexander Kurtakov <akurtako@redhat.com> 1.8.1-9
- Build with maven 3.
- Adapt to current guidelines.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri May 21 2010 Mat Booth <fedora@matbooth.co.uk> - 1.8.1-7
- Correct dep-map names.

* Fri May 14 2010 Mat Booth <fedora@matbooth.co.uk> - 1.8.1-6
- Obsolete jakarta javadoc package.
- Keep legacy depmap around.

* Thu May 13 2010 Mat Booth <fedora@matbooth.co.uk> - 1.8.1-5
- Drop really old obsoletes/provides on short_name.
- Fix requires.

* Tue May 11 2010 Mat Booth <fedora@matbooth.co.uk> - 1.8.1-4
- Not ready for auto OSGi depsolving yet in this package.
- Rename package (jakarta-commons-digester->apache-commons-digester).

* Tue Dec 8 2009 Mat Booth <fedora@matbooth.co.uk> - 1.8.1-3
- Enable OSGi automatic depsolving (from Alphonse Van Assche).

* Sun Nov 8 2009 Mat Booth <fedora@matbooth.co.uk> - 1.8.1-2
- Fix build failure due to targeting too old a JRE
- Add missing doxia build req

* Sun Nov 8 2009 Mat Booth <fedora@matbooth.co.uk> - 1.8.1-1
- Update to 1.8.1
- Rewrite spec file to build using upstream-preferred maven instead of ant
- Install pom and add to maven dep-map
- Fix javadoc package requires

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 0:1.7-10.3
- Convert specfile to UTF-8.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.7-9.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.7-8.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.7-7.3
- fix license tag
- drop repotag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:1.7-7jpp.2
- Autorebuild for GCC 4.3

* Fri Sep 07 2007 Matt Wringe <mwringe@redhat.com> - 0:1.7-6jpp.2
- Fix unowned dir (/usr/lib/gcj/jakarta-commons-digester)

* Mon Jan 22 2007 Vivek Lakshmanan <vivekl at redhat.com> - 0:1.7-6jpp.1
- Resynch with JPP release

* Tue Jan 16 2007 Vivek Lakshmanan <vivekl at redhat.com> - 0:1.7-5jpp.3
- Update component-info.xml to add scm and tag attribute instead of a comment
- Remove the export of a versioned jar

* Tue Jan 9 2007 Vivek Lakshmanan <vivekl at redhat.com> - 0:1.7-5jpp.2
- Upgrade to latest from JPP and FC6
- Remove old RHUG specific trigger
- Add support for conditional build of repolib package
- Build repolib package by default

* Thu Aug 10 2006 Matt Wringe <mwringe at redhat.com> - 0:1.7-5jpp.1
- Merge with upstream version:
 - Add missing requires for javadoc

* Thu Aug 10 2006 Karsten Hopp <karsten@redhat.de> 1.7-4jpp_3fc
- Requires(post/postun): coreutils

* Sat Jul 22 2006 Jakub Jelinek <jakub@redhat.com> - 0:1.7-4jpp_2fc
- Rebuilt

* Wed Jul 19 2006 Matt Wringe <mwringe at redhat.com> - 0:1.7-4jpp_1fc
- Merged with upstream version

* Wed Jul 19 2006 Matt Wringe <mwringe at redhat.com> - 0:1.7-4jpp
- Removed separate definition of name, version and release.

* Mon Jul 17 2006 Matt Wringe <mwringe at redhat.com> - 0:1.7-3jpp
- Added conditional native compiling

* Wed Apr 26 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.7-2jpp
- First JPP 1.7 build

* Tue Jul 26 2005 Fernando Nasser <fnasser@redhat.com> - 0:1.7-1jpp
- Upgrade to 1.7

* Thu Nov 26 2004 Fernando Nasser <fnasser@redhat.com> - 0:1.6-2jpp
- Rebuild so that rss package is included

* Thu Oct 21 2004 Fernando Nasser <fnasser@redhat.com> - 0:1.6-1jpp
- Upgrade to 1.6

* Sun Aug 23 2004 Randy Watler <rwatler at finali.com> - 0:1.5-4jpp
- Rebuild with ant-1.6.2

* Fri May 09 2003 David Walluck <david@anti-microsoft.org> 0:1.5-3jpp
- update for JPackage 1.5

* Thu May 08 2003 Henri Gomez <hgomez@users.sourceforge.net> 1.5-2jpp
- used correct JPP 1.5 spec file

* Thu May 08 2003 Henri Gomez <hgomez@users.sourceforge.net> 1.5-2jpp
- 1.5
