# ANU QRNG Random Password Generator
## Random Password Generator using Quantum Random Number Generation

Generating reliable and secure random password credentials is a difficult problem to solve. If human password generation is used then valuable psychological load is expended, whereas using psuedo-random password generation has entropy convergence concerns.

ANU QRNG is a project which is operated by researchers from the Australian National University, and makes use of quantum physics to generate random numbers using broadband measurements of the vacuum field contained in the radio-frequency sidebands of a single-mode laser.

This handy utility uses the ANU QRNG random number stream to combine psuedo-random and quantum random numbers to generate a password of arbitary length.

Making use of psuedo-random sampling in addition to a quantum random data seed, provides additional guarantees.

## Usage Instructions
- Install `python3` on your machine
- Install `git` on your machine
```bash
git clone https://github.com/asadhasan832/qrng_random_password_generator.git
cd qrng_random_password_generator
./make_password_qrng.py
```

*References:*

[ANU QRNG Project](https://qrng.anu.edu.au/)

[Real time demonstration of high bitrate quantum random number generation with coherent laser light](https://aip.scitation.org/doi/10.1063/1.3597793)

[How to create a strong random password generator in python?](https://www.bhutanpythoncoders.com/how-to-create-a-strong-random-password-generator-in-python/)