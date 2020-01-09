%define openjadever 1.3.2
%define version_list "{3,4}.{0,1}-sgml 4.1.2-xml 4.{2,3,4,5}-{sgml,xml}"

Name: docbook-dtds
Version: 1.0
Release: 51%{?dist}
Group: Applications/Text

Summary: SGML and XML document type definitions for DocBook

License: Copyright only
URL: http://www.oasis-open.org/docbook/

Obsoletes: docbook-dtd30-sgml < %{version}-%{release}
Obsoletes: docbook-dtd31-sgml < %{version}-%{release}
Obsoletes: docbook-dtd40-sgml < %{version}-%{release}
Obsoletes: docbook-dtd41-sgml < %{version}-%{release}
Obsoletes: docbook-dtd412-xml < %{version}-%{release}

Provides: docbook-dtd-xml = %{version}-%{release}
Provides: docbook-dtd-sgml = %{version}-%{release}
Provides: docbook-dtd30-sgml = %{version}-%{release}
Provides: docbook-dtd31-sgml = %{version}-%{release}
Provides: docbook-dtd40-sgml = %{version}-%{release}
Provides: docbook-dtd41-sgml = %{version}-%{release}
Provides: docbook-dtd412-xml = %{version}-%{release}
Provides: docbook-dtd42-sgml = %{version}-%{release}
Provides: docbook-dtd42-xml = %{version}-%{release}
Provides: docbook-dtd43-sgml = %{version}-%{release}
Provides: docbook-dtd43-xml = %{version}-%{release}
Provides: docbook-dtd44-sgml = %{version}-%{release}
Provides: docbook-dtd44-xml = %{version}-%{release}
Provides: docbook-dtd45-sgml = %{version}-%{release}
Provides: docbook-dtd45-xml = %{version}-%{release}

Requires(post): libxml2 >= 2.4.8
Requires(postun): libxml2 >= 2.4.8
Requires(post): sed
Requires(postun): sed
# If upgrading, the old package's postun scriptlet may use install-catalog
# to remove its entries.  xmlcatalog (which this package uses) adds quotes
# to the catalog files, and install-catalog only handles this in 0.6.3-4 or
# later.
Requires(post): /bin/chmod
Requires: sgml-common >= 0.6.3-4
# We provide the directory layout expected by 0.6.3-5 or later of
# xml-common.  Earlier versions won't understand. Additionally
# require xml-common >= 0.6.3-24 to workaround issue with F9
# install+update and empty xmlcatalog
Requires: xml-common >= 0.6.3-24

BuildRoot: %{_tmppath}/%{name}-%{version}

BuildArch: noarch
Source0: http://www.oasis-open.org/docbook/sgml/3.0/docbk30.zip
Source1: http://www.oasis-open.org/docbook/sgml/3.1/docbk31.zip
Source2: http://www.oasis-open.org/docbook/sgml/4.0/docbk40.zip
Source3: http://www.oasis-open.org/docbook/sgml/4.1/docbk41.zip
Source4: http://www.oasis-open.org/docbook/xml/4.1.2/docbkx412.zip
Source5: http://www.oasis-open.org/docbook/sgml/4.2/docbook-4.2.zip
Source6: http://www.oasis-open.org/docbook/xml/4.2/docbook-xml-4.2.zip
Source7: http://www.docbook.org/sgml/4.3/docbook-4.3.zip
Source8: http://www.docbook.org/xml/4.3/docbook-xml-4.3.zip
Source9: http://www.docbook.org/sgml/4.4/docbook-4.4.zip
Source10: http://www.docbook.org/xml/4.4/docbook-xml-4.4.zip
Source11: http://www.docbook.org/sgml/4.5/docbook-4.5.zip
Source12: http://www.docbook.org/xml/4.5/docbook-xml-4.5.zip
#fix old catalog files
Patch0: docbook-dtd30-sgml-1.0.catalog.patch
Patch1: docbook-dtd31-sgml-1.0.catalog.patch
Patch2: docbook-dtd40-sgml-1.0.catalog.patch
Patch3: docbook-dtd41-sgml-1.0.catalog.patch
Patch4: docbook-dtd42-sgml-1.0.catalog.patch
#fix euro sign in 4.2 dtds
Patch5: docbook-4.2-euro.patch
#Fix ISO entities in 4.3/4.4/4.5 SGML
Patch6: docbook-dtds-ents.patch
#Use system rewrite for web URL's in sgml catalogs to prevent reading from the network(#478680)
Patch7: docbook-sgml-systemrewrite.patch
#use XML at the end of public identificators of XML 4.1.2 ISO entities
Patch8: docbook-dtd412-entities.patch
BuildRequires: unzip

%description
The DocBook Document Type Definition (DTD) describes the syntax of
technical documentation texts (articles, books and manual pages).
This syntax is XML-compliant and is developed by the OASIS consortium.
This package contains SGML and XML versions of the DocBook DTD.


%prep
%setup -c -T
eval mkdir %{version_list}
# DocBook V3.0
cd 3.0-sgml
unzip %{SOURCE0}
patch -b docbook.cat %{PATCH0}
cd ..

# DocBook V3.1
cd 3.1-sgml
unzip %{SOURCE1}
patch -b docbook.cat %{PATCH1}
cd ..

# DocBook V4.0
cd 4.0-sgml
unzip %{SOURCE2}
patch -b docbook.cat %{PATCH2}
cd ..

# DocBook V4.1
cd 4.1-sgml
unzip %{SOURCE3}
patch -b docbook.cat %{PATCH3}
cd ..

# DocBook XML V4.1.2
cd 4.1.2-xml
unzip %{SOURCE4}
cd ..

# DocBook V4.2
cd 4.2-sgml
unzip %{SOURCE5}
patch -b docbook.cat %{PATCH4}
cd ..

# DocBook XML V4.2
cd 4.2-xml
unzip %{SOURCE6}
cd ..

# DocBook V4.3
cd 4.3-sgml
unzip %{SOURCE7}
cd ..

# DocBook XML V4.3
cd 4.3-xml
unzip %{SOURCE8}
cd ..

# DocBook V4.4
cd 4.4-sgml
unzip %{SOURCE9}
cd ..

# DocBook XML V4.4
cd 4.4-xml
unzip %{SOURCE10}
cd ..

# DocBook v4.5
cd 4.5-sgml
unzip %{SOURCE11}
cd ..

# DocBook XML v4.5
cd 4.5-xml
unzip %{SOURCE12}
cd ..

# Fix &euro; in SGML.
%patch5 -p1

# Fix ISO entities in 4.3/4.4/4.5 SGML
%patch6 -p1

# Rewrite SYSTEM to use local catalog instead web ones (#478680)
%patch7 -p1

# Add XML to the end of public identificators of 4.1.2 XML entities
%patch8 -p1

# Increase NAMELEN (bug #36058, bug #159382).
sed -e's,\(NAMELEN\s\+\)44\(\s\*\)\?,\1256,' -i.namelen */docbook.dcl

# fix of \r\n issue from rpmlint
sed -i 's/\r//' */*.txt


if [ `id -u` -eq 0 ]; then
  chown -R root:root .
  chmod -R a+rX,g-w,o-w .
fi


%build


%install
rm -rf $RPM_BUILD_ROOT

# Symlinks
mkdir -p $RPM_BUILD_ROOT/etc/sgml
for fmt in sgml xml; do
  ln -s $fmt-docbook-4.5-%{version}-%{release}.cat \
     $RPM_BUILD_ROOT/etc/sgml/$fmt-docbook.cat
done

eval set %{version_list}
for dir
do
  cd $dir
  fmt=${dir#*-} vvr=${dir%%-*}-%{version}-%{release}
  DESTDIR=$RPM_BUILD_ROOT/usr/share/sgml/docbook/$fmt-dtd-$vvr
  case $fmt in
    sgml)   mkdir -p $DESTDIR ; install *.dcl $DESTDIR ;;
    xml)    mkdir -p $DESTDIR/ent ; install ent/* $DESTDIR/ent ;;
  esac
  install *.dtd *.mod $DESTDIR
  install docbook.cat $DESTDIR/catalog
  cd ..
  # File for %%ghost
  touch $RPM_BUILD_ROOT/etc/sgml/$fmt-docbook-$vvr.cat
done


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr (0644,root,root,0755)
#in upstream tarballs there is a lot of files with 0755 permissions
#but they don't need to be, 0644 is enough for every file in tarball
%doc --parents 3.1-sgml/ChangeLog 4.1-sgml/ChangeLog */*.txt
%config(noreplace) /etc/sgml/sgml-docbook.cat
%config(noreplace) /etc/sgml/xml-docbook.cat
/usr/share/sgml/docbook/*ml-dtd-*-%{version}-%{release}
%ghost %config(noreplace) /etc/sgml/*ml-docbook-*-%{version}-%{release}.cat


%post
catcmd='/usr/bin/xmlcatalog --noout'
xmlcatalog=/usr/share/sgml/docbook/xmlcatalog

## Clean up pre-docbook-dtds mess caused by broken trigger.
for v in 3.0 3.1 4.0 4.1 4.2
do
  if [ -f /etc/sgml/sgml-docbook-$v.cat ]
  then
    $catcmd --sgml --del /etc/sgml/sgml-docbook-$v.cat \
      /usr/share/sgml/openjade-1.3.1/catalog 2>/dev/null
  fi
done

# The STYLESHEETS/catalog command is for the case in which the style sheets
# were installed after another DTD but before this DTD
for STYLESHEETS in /usr/share/sgml/docbook/dsssl-stylesheets-*; do : ; done
case $STYLESHEETS in
  *-"*") STYLESHEETS= ;;
esac
eval set %{version_list}
for dir
do
  fmt=${dir#*-} ver=${dir%%-*} vvr=$ver-%{version}-%{release}
  sgmldir=/usr/share/sgml/docbook/$fmt-dtd-$vvr
  ## SGML catalog
  # Update the centralized catalog corresponding to this version of the DTD
  for cat_dir in /usr/share/sgml/sgml-iso-entities-8879.1986 $sgmldir $STYLESHEETS; do
    $catcmd --sgml --add /etc/sgml/$fmt-docbook-$vvr.cat $cat_dir/catalog
  done
  ## XML catalog
  if [ $fmt = xml -a -w $xmlcatalog ]; then
    while read f desc; do
      case $ver in 4.[45]) f=${f/-/} ;; esac
      $catcmd --add public "$desc" $sgmldir/$f $xmlcatalog
    done <<ENDENT
      ent/iso-pub.ent	ISO 8879:1986//ENTITIES Publishing//EN
      ent/iso-grk1.ent	ISO 8879:1986//ENTITIES Greek Letters//EN
      dbpoolx.mod	-//OASIS//ELEMENTS DocBook XML Information Pool V$ver//EN
      ent/iso-box.ent	ISO 8879:1986//ENTITIES Box and Line Drawing//EN
      docbookx.dtd	-//OASIS//DTD DocBook XML V$ver//EN
      ent/iso-grk3.ent	ISO 8879:1986//ENTITIES Greek Symbols//EN
      ent/iso-amsn.ent	ISO 8879:1986//ENTITIES Added Math Symbols: Negated Relations//EN
      ent/iso-num.ent	ISO 8879:1986//ENTITIES Numeric and Special Graphic//EN
      dbcentx.mod	-//OASIS//ENTITIES DocBook XML Character Entities V$ver//EN
      ent/iso-grk4.ent	ISO 8879:1986//ENTITIES Alternative Greek Symbols//EN
      dbnotnx.mod	-//OASIS//ENTITIES DocBook XML Notations V$ver//EN
      ent/iso-dia.ent	ISO 8879:1986//ENTITIES Diacritical Marks//EN
      ent/iso-grk2.ent	ISO 8879:1986//ENTITIES Monotoniko Greek//EN
      dbgenent.mod	-//OASIS//ENTITIES DocBook XML Additional General Entities V$ver//EN
      dbhierx.mod	-//OASIS//ELEMENTS DocBook XML Document Hierarchy V$ver//EN
      ent/iso-amsa.ent	ISO 8879:1986//ENTITIES Added Math Symbols: Arrow Relations//EN
      ent/iso-amso.ent	ISO 8879:1986//ENTITIES Added Math Symbols: Ordinary//EN
      ent/iso-cyr1.ent	ISO 8879:1986//ENTITIES Russian Cyrillic//EN
      ent/iso-tech.ent	ISO 8879:1986//ENTITIES General Technical//EN
      ent/iso-amsc.ent	ISO 8879:1986//ENTITIES Added Math Symbols: Delimiters//EN
      soextblx.dtd	-//OASIS//DTD XML Exchange Table Model 19990315//EN
      calstblx.dtd	-//OASIS//DTD DocBook XML CALS Table Model V$ver//EN
      ent/iso-lat1.ent	ISO 8879:1986//ENTITIES Added Latin 1//EN
      ent/iso-amsb.ent	ISO 8879:1986//ENTITIES Added Math Symbols: Binary Operators//EN
      ent/iso-lat2.ent	ISO 8879:1986//ENTITIES Added Latin 2//EN
      ent/iso-amsr.ent	ISO 8879:1986//ENTITIES Added Math Symbols: Relations//EN
      ent/iso-cyr2.ent	ISO 8879:1986//ENTITIES Non-Russian Cyrillic//EN
ENDENT
    for f in System URI; do
      $catcmd --add rewrite$f "http://www.oasis-open.org/docbook/xml/$ver" \
	$sgmldir $xmlcatalog
    done
  fi
done

# Historic versions of this scriptlet contained the following comment:
# <quote>
# Fix up SGML super catalog so that there isn't an XML DTD before an
# SGML one.  We need to do this (*sigh*) because xmlcatalog messes up
# the order of the lines, and SGML tools don't like to see XML things
# they aren't expecting.
# </quote>
# But the code that followed just found the first XML DTD and the first
# SGML DTD, swappinmg these two lines if the XML one preceded.
# But that only ensures that there is an SGML DTD before all XML ones.
# No one complained, so either this was enough, or the buggy SGML tools
# are long dead, or their users do not use bugzilla.
# Anyway, the following code, introduced in 1.0-46, does better: it ensures
# that all XML DTDs are after all SGML ones, by moving them to the end.
sed -ni '
  /xml-docbook/ H
  /xml-docbook/ !p
  $ {
          g
          s/^\n//p
  }
  ' /etc/sgml/catalog

# Finally, make sure everything in /etc/sgml is readable!
/bin/chmod a+r /etc/sgml/*

%postun
catcmd='/usr/bin/xmlcatalog --noout'
xmlcatalog=/usr/share/sgml/docbook/xmlcatalog
entities="
ent/iso-pub.ent
ent/iso-grk1.ent
dbpoolx.mod
ent/iso-box.ent
docbookx.dtd
ent/iso-grk3.ent
ent/iso-amsn.ent
ent/iso-num.ent
dbcentx.mod
ent/iso-grk4.ent
dbnotnx.mod
ent/iso-dia.ent
ent/iso-grk2.ent
dbgenent.mod
dbhierx.mod
ent/iso-amsa.ent
ent/iso-amso.ent
ent/iso-cyr1.ent
ent/iso-tech.ent
ent/iso-amsc.ent
soextblx.dtd
calstblx.dtd
ent/iso-lat1.ent
ent/iso-amsb.ent
ent/iso-lat2.ent
ent/iso-amsr.ent
ent/iso-cyr2.ent
"
eval set %{version_list}
for dir
do
  fmt=${dir#*-} ver=${dir%%-*} vvr=$ver-%{version}-%{release}
  sgmldir=/usr/share/sgml/docbook/$fmt-dtd-$vvr
  ## SGML catalog
  # Update the centralized catalog corresponding to this version of the DTD
  $catcmd --sgml --del /etc/sgml/catalog /etc/sgml/$fmt-docbook-$vvr.cat
  rm -f /etc/sgml/$fmt-docbook-$vvr.cat
  ## XML catalog
  if [ $fmt = xml -a -w $xmlcatalog ]; then
    for f in $entities; do
      case $ver in 4.[45]) f=${f/-/} ;; esac
      $catcmd --del $sgmldir/$f $xmlcatalog
    done
    $catcmd --del $sgmldir $xmlcatalog
  fi
done

# See the comment attached to this command in the %%post scriptlet.
sed -ni '
  /xml-docbook/ H
  /xml-docbook/ !p
  $ {
          g
          s/^\n//p
  }
  ' /etc/sgml/catalog

%triggerin -- openjade >= %{openjadever}
eval set %{version_list}
for dir
do
  fmt=${dir#*-} ver=${dir%%-*} vvr=$ver-%{version}-%{release}
  /usr/bin/xmlcatalog --sgml --noout --add /etc/sgml/$fmt-docbook-$vvr.cat \
    /usr/share/sgml/openjade-%{openjadever}/catalog
done

%triggerun -- openjade >= %{openjadever}
[ $2 = 0 ] || exit 0
eval set %{version_list}
for dir
do
  fmt=${dir#*-} ver=${dir%%-*} vvr=$ver-%{version}-%{release}
  /usr/bin/xmlcatalog --sgml --noout --del /etc/sgml/$fmt-docbook-$vvr.cat \
    /usr/share/sgml/openjade-%{openjadever}/catalog
done

%changelog
* Tue May 18 2010 Ondrej Vasik <ovasik@redhat.com> - 1.0-51
- post and postun scriptlet requires sed (#593078)

* Thu Dec 17 2009 Ondrej Vasik <ovasik@redhat.com> - 1.0-50
- comment patches
- License: Copyright only

* Tue Oct 27 2009 Ondrej Vasik <ovasik@redhat.com> - 1.0-49
- do not obsolete self

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 11 2009 Ondrej Vasik <ovasik@redhat.com> - 1.0-47
- add requires(post) for /bin/chmod (#498680)

* Wed Apr  8 2009 Stepan Kasal <skasal@redhat.com> - 1.0-46
- remove perl dependency (#462997)
- make %%install and the scriptlets more compact

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Ondrej Vasik <ovasik@redhat.com> - 1.0.44
- fix ISO entities for 4.5 SGML, use XML at the end of
  public identificators of XML 4.1.2 ISO entities

* Thu Feb 19 2009 Ondrej Vasik <ovasik@redhat.com> - 1.0-43
- register sgml catalogs before xml catalogs in openjade
  (#486257)

* Thu Feb 05 2009 Ondrej Vasik <ovasik@redhat.com> - 1.0-42
- Use SYSTEM rewrite for web URL's in sgml catalogs to
  prevent reading from the network(#478680)

* Fri Sep 26 2008 Ondrej Vasik <ovasik@redhat.com> - 1.0-41
- Removed openjade requirement - registration reworked to
  triggers(#234345)

* Wed Sep 24 2008 Ondrej Vasik <ovasik@redhat.com> - 1.0-40
- Fix wrong filenames for xml-dtd-4.4 and xml-dtd-4.5
  iso entities(#461206)
- /ent/iso-cyr1.ent now correctly registered in xml catalog
  (there was /ent/iso-cyrl.ent typo)
- fixed broken unregistration of xml-dtds from catalog
  (missing CAT_DIR variable)

* Fri Aug 29 2008 Ondrej Vasik <ovasik@redhat.com> - 1.0-39
- rebuild with F9 spec file to fix some heavy-weight black
  magic causing failures of sgml documents

* Fri Jul 11 2008 Ondrej Vasik <ovasik@redhat.com> - 1.0-38
- fixed typo in post scriptlet(causing mishandling of DocBook
  4.4 and 4.5 DTDs,#453513)

* Wed Jul 09 2008 Ondrej Vasik <ovasik@redhat.com> - 1.0-37
- use full paths in xmlcatalog registration

* Tue May 13 2008 Ondrej Vasik <ovasik@redhat.com> - 1.0-36
- changed License(#445008)

* Mon Nov 26 2007 Ondrej Vasik <ovasik@redhat.com> - 1.0-35
- fixed bug causing typo in spec file(#397651)

* Tue Oct 23 2007 Ondrej Vasik <ovasik@redhat.com> - 1.0-34
- corrected most of rpmlint issues
- (PreReq, tab/spaces , wrong permissions on some files,
-  wrong file end encoding of txt files, non config files
-  in /etc, some requires issues, versioned provides and
-  obsoletes, fixed license tag)

* Fri Oct 19 2007 Ondrej Vasik <ovasik@redhat.com> - 1.0-33
- fixed wrong attributes for docs(#326581)

* Mon Oct  1 2007 Ondrej Vasik <ovasik@redhat.com> - 1.0-32
- DocBook 4.5 SGML and XML.(#312941)
- added dist tag

* Wed Jun 20 2007 Ondrej Vasik <ovasik@redhat.com> - 1.0-31
- .cat files touched and ghosted to be owned by package
- (bug #193475)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.0-30.1
- rebuild

* Tue Dec 13 2005 Tim Waugh <twaugh@redhat.com> 1.0-30
- Fix ISO entities in 4.3/4.4 SGML.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Oct 21 2005 Tim Waugh <twaugh@redhat.com> 1.0-29
- Scriptlet fix (bug #171229).

* Thu Oct 13 2005 Tim Waugh <twaugh@redhat.com> 1.0-28
- Fixed last fix (bug #159382).

* Thu Jun  2 2005 Tim Waugh <twaugh@redhat.com> 1.0-27
- Increase NAMELEN (bug #36058, bug #159382).

* Tue Feb  1 2005 Tim Waugh <twaugh@redhat.com> 1.0-26
- DocBook 4.4 SGML and XML.

* Mon Sep 13 2004 Tim Waugh <twaugh@redhat.com> 1.0-25
- DocBook 4.3 SGML and XML (bug #131861).

* Mon Feb 23 2004 Tim Waugh <twaugh@redhat.com> 1.0-24
- Use ':' instead of '.' as separator for chown.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Aug  6 2003 Tim Waugh <twaugh@redhat.com> 1.0-22.1
- Rebuilt.

* Wed Aug  6 2003 Tim Waugh <twaugh@redhat.com> 1.0-22
- More work-arounds for buggy xmlcatalog.

* Tue Jul 15 2003 Tim Waugh <twaugh@redhat.com> 1.0-21.1
- Rebuilt.

* Tue Jul 15 2003 Tim Waugh <twaugh@redhat.com> 1.0-21
- Fix &euro; in SGML tools.

* Wed May 28 2003 Tim Waugh <twaugh@redhat.com> 1.0-20
- Fix summary and description (bug #73005).

* Fri Mar 28 2003 Tim Waugh <twaugh@redhat.com> 1.0-19
- Use --parents in %%doc.
- Fix %%postun scriptlet.

* Fri Mar 14 2003 Tim Waugh <twaugh@redhat.com> 1.0-18
- Use Requires:, not Conflicts:, for openjade.
- Require openjade 1.3.2.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 1.0-17
- rebuilt

* Fri Dec 20 2002 Tim Waugh <twaugh@redhat.com> 1.0-16
- Fix typos in scriplets (bug #80109).

* Wed Nov 20 2002 Tim Powers <timp@redhat.com> 1.0-15
- rebuild in current collinst

* Mon Jul 30 2002 Tim Waugh <twaugh@redhat.com> 1.0-14
- Fix typo in XML catalog (Eric Raymond).

* Tue Jul 23 2002 Tim Waugh <twaugh@redhat.com> 1.0-13
- Provide docbook-dtd42-sgml and docbook-dtd42-xml.

* Thu Jul 18 2002 Tim Waugh <twaugh@redhat.com> 1.0-12
- Fix up SGML super catalog if necessary.

* Wed Jul 17 2002 Tim Waugh <twaugh@redhat.com> 1.0-11
- Add DocBook V4.2.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 1.0-10
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com> 1.0-9
- automated rebuild

* Thu Mar 14 2002 Tim Waugh <twaugh@redhat.com> 1.0-8
- Allow for shared /usr/share (bug #61147).

* Tue Mar 12 2002 Tim Waugh <twaugh@redhat.com> 1.0-7
- Make sure that the config files are readable.

* Fri Mar  8 2002 Tim Waugh <twaugh@redhat.com> 1.0-6
- Make %%post scriptlet quiet (bug #60820).

* Thu Feb 21 2002 Tim Waugh <twaugh@redhat.com> 1.0-5
- Make sure to clean up old catalog files.

* Thu Feb 21 2002 Tim Waugh <twaugh@redhat.com> 1.0-3
- Rebuild in new environment.

* Mon Jan 28 2002 Tim Waugh <twaugh@redhat.com> 1.0-2
- Prepare for openjade 1.3.1.

* Thu Jan 17 2002 Tim Waugh <twaugh@redhat.com> 1.0-1
- Merged all the DTD packages into one (bug #58448).
- Use /usr/share/sgml exclusively.
- Prevent catalog files from disappearing on upgrade (bug #58463).

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Nov  5 2001 Tim Waugh <twaugh@redhat.com> 1.0-8
- Hmm, still need to depend on sgml-common for /etc/sgml.

* Mon Nov  5 2001 Tim Waugh <twaugh@redhat.com> 1.0-7
- Use xmlcatalog (libxml2) instead of install-catalog (sgml-common) in
  scriptlets.
- Conflict with install-catalog if it can't handle quotes in catalogs.
- Use release number in centralized catalog name, so that the scriptlets
  work properly.

* Wed Oct 10 2001 Tim Waugh <twaugh@redhat.com> 1.0-6
- Change some Requires: to PreReq:s (bug #54507).

* Mon Oct  8 2001 Tim Waugh <twaugh@redhat.com> 1.0-5
- Use release number in the installed directory name, so that the
  package scripts work.

* Sat Oct  6 2001 Tim Waugh <twaugh@redhat.com> 1.0-4
- Restore the /etc/sgml/catalog manipulation again.
- Oops, fix DTD path.

* Sat Oct  6 2001 Tim Waugh <twaugh@redhat.com> 1.0-2
- Require xml-common.  Use xmlcatalog.
- Move files to /usr/share/xml.

* Tue Jun 12 2001 Tim Waugh <twaugh@redhat.com> 1.0-1
- Build for Red Hat Linux.

* Sat Jun 09 2001 Chris Runge <crunge@pobox.com>
- Provides: docbook-dtd-xml (not docbook-dtd-sgml)
- undo catalog patch and dbcentx patch (this resulted in an effectively
  broken DTD when the document was processed with XSL stylesheets); added a
  symbolic link to retain docbook.cat -> catalog; added ent
- added ChangeLog to doc

* Fri Jun 08 2001 Chris Runge <crunge@pobox.com>
- created a 4.1.2 version
- update required a change to OTHERCAT in postun
- update required a change to the Makefile patch (no dbgenent.ent any more,
  apparently)

* Wed Jan 24 2001 Tim Waugh <twaugh@redhat.com>
- Scripts require fileutils.
- Make scripts quieter.

* Mon Jan 15 2001 Tim Waugh <twaugh@redhat.com>
- Don't play so many macro games.
- Don't use 'rpm' in post scripts.
- Be sure to own xml-dtd-4.1 directory.

* Sun Jan 14 2001 Tim Waugh <twaugh@redhat.com>
- Change requirement on /usr/bin/install-catalog to sgml-common.

* Tue Jan 09 2001 Tim Waugh <twaugh@redhat.com>
- Change group.
- Use %%{_tmppath}.
- Correct typo.
- rm before install
- openjade not jade.
- Build requires unzip.
- Require install-catalog for post and postun.
- Change Copyright: to License:.
- Remove Packager: line.

* Tue Jan 09 2001 Tim Waugh <twaugh@redhat.com>
- Based on Eric Bischoff's new-trials packages.
