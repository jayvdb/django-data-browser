import React, { useState, useEffect } from "react";
import "./App.css";
import { TLink, SLink } from "./Util.js";
import { Results } from "./Results.js";
import { Link } from "react-router-dom";

function FilterValue(props) {
  const { lookup, onChange, value } = props;
  if (props.lookup.type === "boolean")
    return (
      <select {...{ onChange, value }} className="FilterValue">
        <option value={true}>true</option>
        <option value={false}>false</option>
      </select>
    );
  else if (lookup.type === "weekday")
    return (
      <select {...{ onChange, value }} className="FilterValue">
        {[
          "Sunday",
          "Monday",
          "Tuesday",
          "Wednesday",
          "Thursday",
          "Friday",
          "Saturday",
        ].map((weekday) => (
          <option value={weekday}>{weekday}</option>
        ))}
      </select>
    );
  else if (lookup.type === "month")
    return (
      <select {...{ onChange, value }} className="FilterValue">
        {[
          "January",
          "Febuary",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December",
        ].map((month) => (
          <option value={month}>{month}</option>
        ))}
      </select>
    );
  else if (lookup.type === "number" || lookup.type === "year")
    return (
      <input
        {...{ onChange, value }}
        className="FilterValue"
        type="number"
        step="0"
      />
    );
  else
    return (
      <input {...{ onChange, value }} className="FilterValue" type="text" />
    );
}

class Filter extends React.Component {
  render() {
    const {
      path,
      prettyPath,
      index,
      lookup,
      query,
      value,
      errorMessage,
    } = this.props;
    const type = query.getType(query.getField(path));
    return (
      <tr>
        <td>
          <SLink onClick={() => query.removeFilter(index)}>close</SLink>{" "}
          <TLink onClick={() => query.addField(path, prettyPath)}>
            {prettyPath.join(" ")}
          </TLink>{" "}
        </td>
        <td>
          <select
            className="Lookup"
            value={lookup}
            onChange={(e) => query.setFilterLookup(index, e.target.value)}
          >
            {type.sortedLookups.map((lookupName) => (
              <option key={lookupName} value={lookupName}>
                {lookupName.replace(/_/g, " ")}
              </option>
            ))}
          </select>
        </td>
        <td>=</td>
        <td>
          <FilterValue
            {...{ value }}
            onChange={(e) => query.setFilterValue(index, e.target.value)}
            lookup={type.lookups[lookup]}
          />
          {errorMessage && <p>{errorMessage}</p>}
        </td>
      </tr>
    );
  }
}

function Filters(props) {
  const { query, filterErrors } = props;
  return (
    <form className="Filters">
      <table className="Flat">
        <tbody>
          {props.filters.map((filter, index) => (
            <Filter
              {...{ query, index }}
              {...filter}
              key={index}
              errorMessage={filterErrors[index]}
            />
          ))}
        </tbody>
      </table>
    </form>
  );
}

class Field extends React.Component {
  constructor(props) {
    super(props);
    this.state = { toggled: false };
  }

  toggle() {
    this.setState((state) => ({
      toggled: !state.toggled,
    }));
  }

  render() {
    const { query, path, prettyPath, modelField } = this.props;
    const type = query.getType(modelField);
    return (
      <>
        <tr>
          <td>
            {modelField.concrete && type.defaultLookup && (
              <SLink onClick={() => query.addFilter(path, prettyPath)}>
                filter_alt
              </SLink>
            )}
          </td>
          <td>
            {modelField.model && (
              <SLink className="ToggleLink" onClick={this.toggle.bind(this)}>
                {this.state.toggled ? "remove" : "add"}
              </SLink>
            )}
          </td>
          <td>
            {modelField.type ? (
              <TLink onClick={() => query.addField(path, prettyPath)}>
                {modelField.prettyName}
              </TLink>
            ) : (
              modelField.prettyName
            )}
          </td>
        </tr>
        {this.state.toggled && (
          <tr>
            <td></td>
            <td colSpan="2">
              <AllFields
                {...{ query, path, prettyPath }}
                model={modelField.model}
              />
            </td>
          </tr>
        )}
      </>
    );
  }
}

function AllFields(props) {
  const { query, model, path, prettyPath } = props;
  const modelFields = query.getModelFields(model);
  return (
    <table>
      <tbody>
        {modelFields.sortedFields.map((fieldName) => {
          const modelField = modelFields.fields[fieldName];
          return (
            <Field
              key={fieldName}
              {...{ query, modelField }}
              path={path.concat([fieldName])}
              prettyPath={prettyPath.concat([modelField.prettyName])}
            />
          );
        })}
      </tbody>
    </table>
  );
}

function ModelSelector(props) {
  return (
    <select
      className="ModelSelector"
      onChange={(e) => props.query.setModel(e.target.value)}
      value={props.model}
    >
      {props.sortedModels.map((model) => (
        <option key={model}>{model}</option>
      ))}
    </select>
  );
}

function Logo(props) {
  const { version } = props;
  return (
    <Link to="/" className="Logo">
      <span>DDB</span>
      <span className="Version">v{version}</span>
    </Link>
  );
}

function QueryPage(props) {
  const {
    query,
    rows,
    cols,
    body,
    version,
    sortedModels,
    model,
    filters,
    filterErrors,
  } = props;
  const saveUrl = query.getUrlForSave();
  return (
    <div id="body">
      <Logo {...{ version }} />
      <ModelSelector {...{ query, sortedModels, model }} />
      <Filters {...{ query, filters, filterErrors }} />
      <p>
        Showing {rows.length * cols.length} results -{" "}
        <a href={query.getUrlForMedia("csv")}>Download as CSV</a> -{" "}
        <a href={query.getUrlForMedia("json")}>View as JSON</a>
        {saveUrl && (
          <>
            {" "}
            - <a href={saveUrl}>Save View</a>{" "}
          </>
        )}
      </p>
      <div className="MainSpace">
        <div className="FieldsList">
          <AllFields {...{ query, model }} path={[]} prettyPath={[]} />
        </div>
        {query.rowFields().length || query.colFields().length ? (
          <Results {...{ query, rows, cols, body }} />
        ) : (
          <h2>No fields selected</h2>
        )}
      </div>
    </div>
  );
}

function useData(url) {
  const [data, setData] = useState([]);
  useEffect(() => {
    fetch(url)
      .then((response) => response.json())
      .then((response) => {
        setData(response);
      });
  }, [url]);
  return data;
}

function SavedViewList(props) {
  const { baseUrl } = props;
  const savedViews = useData(`${baseUrl}api/views/`);
  return (
    <div>
      <h1>Saved Views</h1>
      <div>
        {savedViews.map((view, index) => (
          <div key={index}>
            <Link className="Link" to={view.link}>
              {view.model} - {view.name}
            </Link>
            <p>{view.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

function HomePage(props) {
  const { version, sortedModels, baseUrl } = props;
  return (
    <div id="body">
      <Logo {...{ version }} />
      <div className="Index">
        <div>
          <h1>Models</h1>
          <div>
            {sortedModels.map((model) => (
              <div key={model}>
                <Link to={`/query/${model}/.html`} className="Link">
                  {model}
                </Link>
              </div>
            ))}
          </div>
        </div>
        <SavedViewList {...{ baseUrl }} />
      </div>
    </div>
  );
}

export { HomePage, QueryPage };
