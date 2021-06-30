import React from 'react';
import ReactHtmlParser from 'react-html-parser';
import { CodeBlock, monokai } from "react-code-blocks";
import {MathJax, MathJaxContext} from 'better-react-mathjax';

export default class Question extends React.Component {
  constructor() {
    super();
    this.state = {statement: 'undef'};
  }

  componentDidMount() {
    fetch('http://127.0.0.1:8000/question')
        .then(res => res.json())
        .then(data => this.setState({ statement: data.message}));
  }

  transformSpecialTags = (node, idx) => {
    if (node.type === 'tag' && node.name === 'codeblock') {
        const data = node.children[0].data
        return (
            <CodeBlock
                text={data}
                language={node.attribs.language}
                showLineNumbers={true}
                theme={monokai}
            />
        );
    }
    else if (node.type === 'tag' && node.name === 'math') {
        const data = node.children[0].data
        return (
            <MathJaxContext>
                <MathJax inline={true}>{data}</MathJax>
            </MathJaxContext>
        );
    }
    else if (node.type === 'tag' && node.name === 'mathblock') {
        const data = node.children[0].data
        return (
            <MathJaxContext>
                <MathJax>{data}</MathJax>
            </MathJaxContext>
        );
    }
  }

  render() {
    return (
      <div>
        { ReactHtmlParser(this.state.statement, {transform: this.transformSpecialTags}) }
      </div>
    );
  }
}

