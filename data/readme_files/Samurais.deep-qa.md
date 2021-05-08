# Note, this repo is deprecated.

If you are interested in further enhancements and investigations, just watch *Next* repo.

[https://github.com/Samurais/Neural\_Conversation\_Models](https://github.com/Samurais/Neural_Conversation_Models)

# Approaching a Chatbot Service
[![Join the chat at https://gitter.im/chatbot-pilots/DeepQA](https://badges.gitter.im/chatbot-pilots/DeepQA.svg)](https://gitter.im/chatbot-pilots/DeepQA?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) [![Docker Pulls](https://img.shields.io/docker/pulls/samurais/deepqa2.svg?maxAge=2592000)](https://hub.docker.com/r/samurais/deepqa2/) [![Docker Stars](https://img.shields.io/docker/stars/samurais/deepqa2.svg?maxAge=2592000)](https://hub.docker.com/r/samurais/deepqa2/) [![Docker Layers](https://images.microbadger.com/badges/image/samurais/deepqa2.svg)](https://microbadger.com/#/images/samurais/deepqa2)

[![chatoper banner][co-banner-image]][co-url]

[co-banner-image]: https://user-images.githubusercontent.com/3538629/42383104-da925942-8168-11e8-8195-868d5fcec170.png
[co-url]: https://www.chatopera.com

[Part 1: Introduction](http://www.leiphone.com/news/201702/O9PGyImfH1Vq3fxV.html)

[Part 2: Bot Engine](http://www.leiphone.com/news/201702/oY07cF3HVIp7Yo1s.html)

[Part 3: Bot Model](http://www.leiphone.com/news/201702/4OZau7OfcNO0v1u5.html)

> This repository is align with  **Part 3: Bot Model**.

Train and serve QA Model with TensorFlow

Tested with TensorFlow#0.11.0rc2, Python#3.5.

[Install Nvidia Drivers, CUDNn, Python, TensorFlow on Ubuntu 16.04](https://gist.github.com/Samurais/e20a8283708d37f1d7c9a709e9332429)

# DeepQA
Inspired and inherited from [DeepQA](https://github.com/Conchylicultor/DeepQA/issues/44).

# Install deps
```
pip install -r requirements.txt
```

# Install TensorFlow
```
export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.11.0rc2-cp35-cp35m-linux_x86_64.whl
pip install —-upgrade $TF_BINARY_URL
```

# Pre-process data
Process data, build vocabulary, word embedding, conversations, etc.
```
cp config.sample.ini config.ini
python deepqa2/dataset/preprocesser.py
```

Sample Corpus http://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html

# Train Model
Train language model with Seq2seq.
```
cp config.sample.ini config.ini # modify keys
python deepqa2/train.py
```

# Serve Model
Provide RESt API to access language model.
```
cd DeepQA2/save/deeplearning.cobra.vulcan.20170127.175256/deepqa2/serve
cp db.sample.sqlite3 db.sqlite3 
python manage.py runserver 0.0.0.0:8000
```

Access Service with RESt API
```
POST /api/v1/question HTTP/1.1
Host: 127.0.0.1:8000
Content-Type: application/json
Authorization: Basic YWRtaW46cGFzc3dvcmQxMjM=
Cache-Control: no-cache

{"message": "good to know"}

response
{
  "rc": 0,
  "msg": "hello"
}
```

# Train with Docker
## Install 
* [docker](https://docs.docker.com/engine/installation/linux/ubuntu/)
* [nvidia-docker](https://github.com/NVIDIA/nvidia-docker)
## Train
```
docker pull samurais/deepqa2:latest
cd DeepQA2
./scripts/train_with_docker.sh
```
