import React from 'react';

function Linha(Props) {
  return (
    <tr>
        {Props.elements.map((e, index) => 
            <td key={index}>{e}</td>
        )}
    </tr>
  );
}

export default Linha;