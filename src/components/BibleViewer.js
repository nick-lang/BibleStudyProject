import { useState } from "react";
import getBible from "../helpers/getBible";

const BibleViewer = (props) => {
  // const [bibleChapter, setBibleChapter] = useState({})
    let bible = getBible();

    const Genesis1 = (props) => {
      return (
        Object.keys(bible.Genesis[1]).map(verseNum => (
          <div key={verseNum}>{verseNum}: {bible.Genesis[1][verseNum]}</div>
        ))
      )
    }


    return (
    <div>
      <Genesis1/>
    </div>

    );
}

export default BibleViewer;

