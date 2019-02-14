FROM debian

### Minimal Python container
### So logging/io works reliably with Docker
ENV PYTHONUNBUFFERED=1

### Basic Python dev dependencies
### -y means yes for any questions during upgrade
RUN apt-get update && \
  apt-get upgrade -y && \    
  apt-get install python3-pip curl nano -y && \
  pip3 install pandas && \
  pip3 install -i https://test.pypi.org/simple/ lambdata-samirgadkari && \
  python3 -c "import lambdata_samirgadkari; print('Success!')"
