# in-text: bold, italic
# html elements: list, table
# code: inline, block
# equations: inline, block
# media: image, audio, video

def get_question():
    return """
        <h1>Title</h1>
        
        <h2>Section</h2>
        
        <h3>Subsection</h3>
        
        <p><strong>bold</strong>, <em>italics</em></p>
        
        <ul>
            <li>List element 1</li>
            <li>List element 2</li>
            <li>List element 3</li>
        </ul>
        
        <table>
          <tr>
            <th>Firstname</th>
            <th>Lastname</th>
            <th>Age</th>
          </tr>
          <tr>
            <td>Jill</td>
            <td>Smith</td>
            <td>50</td>
          </tr>
          <tr>
            <td>Eve</td>
            <td>Jackson</td>
            <td>94</td>
          </tr>
        </table>
        
        <p>This is an <code>inline-code</code> sample</p>
        
        <p>And this is a block code sample:</p>
        
        <codeblock language='python', type='text'>
            class User:
                def __init__(self, name):
                    self.name = name
        </codeblock>
        
        <p>Inline math: <math>\\(\\frac{10}{4x} \\approx 2^{12}\\)</math></p>
        
        <p>Or a block of math...</p>
        
        <mathblock>
            \\(\\frac{10}{4x} \\approx 2^{12}\\)
        </mathblock>
        
        <p>We can also add images...</p>
        
        <img src='https://i.pinimg.com/originals/6c/08/f8/6c08f858d4025e90881e2cf2da1ec0cb.jpg' width=200 height=150>
        
        <p>But currently I have no idea how to add them inline</p>
    """