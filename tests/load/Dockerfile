FROM centos

CMD ["/bin/bash", "-c", "for i in $(seq 1 ${ITERS:-60}); do curl --fail --silent joker/joke; echo ''; sleep 1; done"]
