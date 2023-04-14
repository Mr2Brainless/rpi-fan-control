.PHONY: all install uninstall purge_config clean

all: build

build:
	@echo "nothing to build"
	@echo "use 'make install' to install"

install: #build
	mkdir -p /usr/local/bin/
	cp fan-control.py /usr/local/bin/
	cp fan-control.conf /etc/
	cp fan-control.service /etc/systemd/system/
	systemctl daemon-reload

	@echo
	@echo "installation complete"
	@echo "enbale with 'systemctl enable fan-control.service' and start with 'systemctl start fan-control.service'"

uninstall:
ifneq ("$(wildcard $(/etc/systemd/system/fan-control.service))","")
	systemctl disable fan-control.service
endif

	rm -f /etc/systemd/system/fan-control.service
	rm -f /usr/local/bin/fan-control.py

purge_config:
	rm -f /etc/fan-control.conf

clean: