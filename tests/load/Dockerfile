FROM centos

CMD ["/bin/bash", "-c", "for i in $(seq 1 ${ITERS:-60}); do curl --silent web/hello; echo ''; sleep 1; done"]
