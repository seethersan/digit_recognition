import React from "react";

export default function SwitchTools({ setToolType, captureCanvas }) {
  return (
    <div>
      <div className="row">
        <div className="col-md-12">
          <div>
            <button
              title="Pencil"
              onClick={() => {
                setToolType("pencil");
              }}
            >
              Pencil
            </button>
            <button
              title="Line"
              onClick={() => {
                setToolType("line");
              }}
            >
              Line
            </button>
            <button
              title="Recognize"
              onClick={() => {
                captureCanvas();
              }}
            >
              Recognize
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}