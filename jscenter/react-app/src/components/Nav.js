import React, { Component } from 'react';

class Nav extends Component {
    render () {
      let data  = this.props.data;
      let i = 0;
      let lists = [];
      while (i < data.length) {
        lists.push(<li><a href={"/content/"+data[i].id}>{data[i].title}</a></li>);
      }
      return (
        <nav>
         <ul>
           {lists}
         </ul>
       </nav>
      )
    }
 }


 export default Nav;
