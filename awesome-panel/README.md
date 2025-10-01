## Links

* https://awesome-panel.org/

* https://awesome-panel.org/resources/table_of_elements_with_wikipedia_row_content/
  * Octoprobe: This table may be used to list tentacles

* https://panel.holoviz.org/reference/widgets/Tabulator.html
  * Octoprobe: This table may be used to list tentacles

* How to
  * https://panel.holoviz.org/how_to/wasm/standalone.html
  * https://panel.holoviz.org/how_to/wasm/convert.html

    To avoid writing all the boilerplate, Panel provides the panel convert command-line interface (CLI).



## Question

python holoviz panel docker: Is there a docker image which spawns up a sample panel application? Please return links to github or dockerhub.

## Answer

Yes, there is a popular community-maintained Docker image that runs a sample **HoloViz Panel** application.

The **Awesome Panel** project maintains a Docker image that powers its website and provides numerous examples of Panel applications running within a container.

### Docker Hub Link

  * **Docker Hub:** `marcskovmadsen/awesome-panel`
      * **Link:** [https://hub.docker.com/r/marcskovmadsen/awesome-panel](https://hub.docker.com/r/marcskovmadsen/awesome-panel)

### GitHub Link

The underlying code for the examples and the Docker setup can be found in the associated GitHub repository, which often includes the `Dockerfile` for reference, although the main Panel framework is on the `holoviz/panel` repository.

  * **GitHub (Awesome Panel Examples):**
      * **Link:** [https://github.com/awesome-panel/examples](https://github.com/awesome-panel/examples)

-----

#### Usage Example

You can run this sample image with the following command (it serves the application on port 80 inside the container, which is mapped to port 80 on your host machine):

```bash
docker run -it -p 80:80 marcskovmadsen/awesome-panel:latest
```

Once running, you can access the gallery of sample applications by navigating to `http://localhost/` in your browser.