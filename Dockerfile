FROM python:3.6
MAINTAINER hewen
ENV TZ=Asia/Shanghai
#创建工作目录
ENV APP_PATH="/app"
ENV PATH /usr/local/bin:$PATH
COPY . $APP_PATH
WORKDIR $APP_PATH
CMD ["python" ,"main.py"]