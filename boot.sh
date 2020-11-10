docker image build -t bot . &&
docker run -p 8081:8081 -e "TZ=Asia/Taipei" bot
