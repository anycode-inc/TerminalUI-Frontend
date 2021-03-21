FROM centos:latest

RUN yum install python3 -y & yum install git -y

RUN pip3 install --upgrade pip

RUN pip3 install flask

EXPOSE 80

RUN git clone https://github.com/anycode-inc/TerminalUI-Frontend.git

RUN cd TerminalUI-Frontend

RUN python3 app.py

CMD /bin/sh