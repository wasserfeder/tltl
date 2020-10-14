# tltl
Truncated Linear Temporal Logic (TLTL)

Setup
-----

```bash
git clone https://github.com/wasserfeder/tltl.git
mkdir -p tltl/lib
cd tltl/lib
wget 'https://www.antlr.org/download/antlr-4.7.1-complete.jar'
pip install antlr4-python2-runtime==4.7.1
```

For permanent settings use:

```bash
cd <clone-dir>
echo "export CLASSPATH=\".:$PWD/lib/antlr-4.7.1-complete.jar:$CLASSPATH\"" >> ~/.bashrc
echo "alias antlr4=\"java -jar $PWD/lib/antlr-4.7.1-complete.jar -visitor\"" >> ~/.bashrc
echo "alias grun=\"java org.antlr.v4.gui.TestRig\"" >> ~/.bashrc
```

Otherwise

```bash
cd <clone-dir>
export CLASSPATH=".:$PWD/lib/antlr-4.7.1-complete.jar:$CLASSPATH"
alias antlr4="java -jar $PWD/lib/antlr-4.7.1-complete.jar -visitor"'
alias grun="java org.antlr.v4.gui.TestRig"
```

where `<clone-dir>` is the directory where you cloned the `tltl` repository.


Run
---

```bash
cd <clone-dir>/src
antlr4 -Dlanguage=Python2 tltl.g4
```

**NOTE:** At the moment the implementation only supports python2. However, you
can generate lexers, parsers, listners, and visitors for other target languages,
such as Java (default), C++, Python3, C#, Go, JavaScript, and Swift.
See http://www.antlr.org/download.html for more details.
