# Container Tutorial

## Resources:
[Anisha Keshavan Docker Tutorial](https://slides.com/anishakeshavan/introduction-to-docker/#/7)

[Nipype Workshop about Containers](http://nipy.org/workshops/2017-03-boston/lectures/lesson-container/#34)

[ReporNim Resource for creating reproducible Environments](http://www.repronim.org/module-dataprocessing/04-containers/)

## Requirements:
[Docker](https://www.docker.com/)

## General Docker Tutorial:

1. Install docker
2. Pull a docker image
```
docker pull hello-world
```
3. Run a docker image
```
docker run hello-world
```
4. Run a docker image, but this time with an interactive terminal (-it) and the image ubuntu with the bash command
```
docker run -it ubuntu bash
```
5. Run a docker image, using the image ubuntu again, with the echo command saying "hello world"
```
docker run ubuntu echo 'hello world'
```
## Image Specific Docker Tutorial:
Many neurimaging pipelines create their own containers and images, so that others, like you and I, can use their materials in a nice, neat reproducible manner. One of these tools we will use is fMRIprep. While we will go into more detail about the use of this resource in subsequent tutorials, in this tutorial, we will practice using fMRIprep via docker.

1. Visit the [fMRIprep website](https://fmriprep.org/en/stable/docker.html#run-docker) to see how this information is referenced
2. Install the Docker Image:
```
python -m pip install --user --upgrade fmriprep-docker
```
3. Pull the latest fMRIPrep Docker images
```
docker pull nipreps/fmriprep:latest
```

**Other important things to know:**

- You can check which containers are currently running by typing
```
docker ps
```
- Adding -a tells you about running and stopped containers
- To stop a container:
```
docker stop <container_id/name>
```
- To remove a stopped container:
```
docker rm <container_id/name> 
```
- Check your images (this is especially important for fmriprep):
```
docker images
```
- Remove an image:
```
docker rmi <image_id>
```

- You can also create and share your own docker images. This tutorial will not cover this aspect, but it is handy. 
