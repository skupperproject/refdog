---
body_class: command
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

## Options

### Output options

- <h4 id="output">--output <span class="argument-info">string</span></h3>

  Print resources to the console instead of submitting
  them to the Skupper controller.

  _Choices:_
  
   - `json` - Produce JSON output
   - `yaml` - Produce YAML output

### Context options

- <h4 id="namespace">--namespace <span class="argument-info">string</span></h3>

  Select the current namespace.

- <h4 id="context">--context <span class="argument-info">string</span></h3>

  Select the current kubeconfig context.

- <h4 id="platform">--platform <span class="argument-info">string</span></h3>

  Select the current Skupper platform.

### Global options

- <h4 id="help">--help <span class="argument-info">None</span></h3>

  Display help and exit.

</section>

<section>

## Errors

</section>
