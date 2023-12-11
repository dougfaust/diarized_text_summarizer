<a name="readme-top"></a>
<!--
*** Diarized text summarizer README.md
-->

<h3 align="center">diarized text summarizer</h3>

  <p align="center">
    project_description
    <br />
    <a href="https://github.com/dougfaust/diarized_text_summarizer"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/dougfaust/diarized_text_summarizer">Installation and use</a>
    ·
    <a href="https://github.com/dougfaust/diarized_text_summarizer/issues">Report Bug</a>
    ·
    <a href="https://github.com/dougfaust/diarized_text_summarizer/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This library provides tools to do "extractive" and "abstractive" text summarization.  The primary goal is a single workflow that allows large amounts of tagged and diarized text such as 

* email and social media threads
* transcripts with multiple speakers
* A/V scripts
* chat logs

to be parsed into single, coherent, summary.

Adapting this to a new purpose simply requires changing extracted text size to be compatable with token limits and changing the parsing or regex to accomodate the thread headers used in the diarized text.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [natural language toolkit](https://www.nltk.org/)
* [huggingface transformers](https://huggingface.co/docs/transformers/index)  

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

1. first install `PyTorch`
   [installing PyTorch locally](https://pytorch.org/get-started/locally/)

2. install huggingface `transforemrs`
If your PyTorch build is cpu only:
  ```sh
  pip install transformers
  ```
or for a full PyTorch build with GPU support
  ```sh
  pip install transformers[torch]
  ```
3. Install `nltk`
   ```sh
   pip install --user -U nltk
   ```

### Installation

After prerequisites are installed, clone this repo
   ```sh
   git clone https://github.com/dougfaust/diarized_text_summarizer.git
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To run on example meeting transcript data, work through the jupyter notebook:

To adapt to a new purpose 

1. catenate data into a single file with time-ordered entries (i.e. the sequence will not be inferred from any timestamps)
   
2. change the regex pattern in to strip the headers or names from your diarized text source.

3. edit extracted text lengths here to a suitable length, limited by the huggingface token limit until coherent summaries are produced.  I wish there was a science to that, but quality of summaries is pretty subjective.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Update to serve LLMs

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

n/a
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/dougfaust/diarized_text_summarizer](https://github.com/dougfaust/diarized_text_summarizer)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

