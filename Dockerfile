FROM centos:latest

RUN yum install python3 -y & yum install git -y

RUN pip3 install --upgrade pip

RUN pip3 install flask

EXPOSE 8080

RUN git clone https://github.com/anycode-inc/TerminalUI-Frontend.git

RUN cd TerminalUI-Frontend

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]