# Mailsac API Examples

This repository contains examples for integrating with the
[Mailsac API](https://mailsac.com/docs/api). The examples are written using
[Node.js](https://nodejs.org/en/download/) which must be setup first. You should
install at least Node version 8.

You will also need a [Mailsac API key](https://mailsac.com/api-keys).

## Getting Started

Clone this repository and navigate to the directory:

```bash
git clone https://github.com/mailsac/mailsac-examples
cd mailsac-examples
```

Now that you are inside the `mailsac-examples` folder and have Node.js installed,
running an example can be done like this:

```bash
MAILSAC_KEY=your_api_key_goes_here node validate-single-email asdf@mailsac.com
```
*(replace `your_api_key_goes_here` with
your key from https://mailsac.com/api-keys)*

## Troubleshooting

Each example has slightly different parameters, and should print what is missing
if you do not supply an expected argument. If you have trouble, try opening
the script up and looking at the usage of `process.argv`.

## License

MIT
