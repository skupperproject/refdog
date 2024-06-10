---
body_class: command
links:
  - name: Listener resource
    url: /resources/listener.html
  - name: Listener command
    url: /commands/listener.html
---

# Listener status command

<section>

Show the status of listeners in the current site.

</section>

<section>

## Usage

~~~ shell
$ skupper listener status
NAME       ROUTING-KEY   HOST       PORT   MATCHING-CONNECTORS
backend    backend       backend    8080   1
database   database      database   5432   1
~~~

</section>

<section>

## Subcommands

</section>

<section>

## Options

### Output options

- <h4 id="output">--output <span class="option-info">string</span></h4>

  Print resources to the console instead of submitting
  them to the Skupper controller.

  _Choices:_
  
   - `json` - Produce JSON output
   - `yaml` - Produce YAML output

### Context options

- <h4 id="namespace">--namespace <span class="option-info">string</span></h4>

  Select the current namespace.

- <h4 id="context">--context <span class="option-info">string</span></h4>

  Select the current kubeconfig context.

- <h4 id="platform">--platform <span class="option-info">string</span></h4>

  Select the current Skupper platform.

### Global options

- <h4 id="help">--help <span class="option-info">None</span></h4>

  Display help and exit.

</section>

<section>

## Errors

</section>
