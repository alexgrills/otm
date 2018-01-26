# One to a Million

Run Tests
~~~~
git clone git@github.com:alexgrills/otm.git
cd otm/
docker build -t otm_test -F Dockerfile.test .
docker run -v $PWD:/otm otm_test pytest
~~~~