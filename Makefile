
all:

install:
	mkdir -p $(DESTDIR)/usr/share/kickstarter-configs/mer/
	mkdir -p $(DESTDIR)/usr/share/kickstarter-configs/mer-reference-images/
	cp rpm-rebuilddb.post $(DESTDIR)/usr/share/kickstarter-configs/mer/
	cp prelink.post $(DESTDIR)/usr/share/kickstarter-configs/mer/
	cp 00base.yaml $(DESTDIR)/usr/share/kickstarter-configs/mer/
	cp 00reference.yaml $(DESTDIR)/usr/share/kickstarter-configs/mer-reference-images/
	cp qmlviewer-session.post $(DESTDIR)/usr/share/kickstarter-configs/mer-reference-images/

clean:
