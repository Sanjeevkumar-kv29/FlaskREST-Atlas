

1 Informational responses (100–199)
2 Successful responses (200–299)
3 Redirects (300–399)
4 Client errors (400–499)
5 Server errors (500–599)



<article class="article"><div><div></div>

<p class="summary"><span class="seoSummary">HTTP response status codes indicate whether a specific <a href="/en-US/docs/Web/HTTP">HTTP</a> request has been successfully completed. Responses are grouped in five classes: </span></p>

<ol>
 <li><span class="seoSummary">Informational responses (<code>100</code>–<code>199</code>)</span></li>
 <li><span class="seoSummary">Successful responses (<code>200</code>–<code>299</code>)</span></li>
 <li><span class="seoSummary">Redirects (<code>300</code>–<code>399</code>)</span></li>
 <li><span class="seoSummary">Client errors (<code>400</code>–<code>499</code>)</span></li>
 <li><span class="seoSummary">Server errors (<code>500</code>–<code>599</code>)</span></li>
</ol>

<p>The below status codes are defined by <a href="https://tools.ietf.org/html/rfc2616#section-10">section 10 of RFC 2616</a>. You can find an updated specification in <a href="https://tools.ietf.org/html/rfc7231#section-6.5.1">RFC 7231</a>.</p>

<div class="notecard note">
<p>If you receive a response that is not in this list, it is a non-standard response, possibly custom to the server's software.</p>
</div></div><h2 id="information_responses"><a href="#information_responses" title="Permalink to Information responses">Information responses</a></h2><div><dl>
 <dt><a href="/en-US/docs/Web/HTTP/Status/100"><code>100 Continue</code></a></dt>
 <dd>This interim response indicates that everything so far is OK and that the client should continue the request, or ignore the response if the request is already finished.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/101"><code>101 Switching Protocol</code></a></dt>
 <dd>This code is sent in response to an <a href="/en-US/docs/Web/HTTP/Headers/Upgrade"><code>Upgrade</code></a> request header from the client, and indicates the protocol the server is switching to.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/102"><code>102 Processing</code></a> (<a href="/en-US/docs/Glossary/WebDAV">WebDAV</a>)</dt>
 <dd>This code indicates that the server has received and is processing the request, but no response is available yet.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/103"><code>103 Early Hints</code></a></dt>
 <dd>This status code is primarily intended to be used with the <a href="/en-US/docs/Web/HTTP/Headers/Link"><code>Link</code></a> header, letting the user agent start <a href="/en-US/docs/Web/HTML/Preloading_content">preloading</a> resources while the server prepares a response.</dd>
</dl></div><h2 id="successful_responses"><a href="#successful_responses" title="Permalink to Successful responses">Successful responses</a></h2><div><dl>
 <dt><a href="/en-US/docs/Web/HTTP/Status/200"><code>200 OK</code></a></dt>
 <dd>The request has succeeded. The meaning of the success depends on the HTTP method:
 <ul>
  <li><code>GET</code>: The resource has been fetched and is transmitted in the message body.</li>
  <li><code>HEAD</code>: The entity headers are in the message body.</li>
  <li><code>PUT</code> or <code>POST</code>: The resource describing the result of the action is transmitted in the message body.</li>
  <li><code>TRACE</code>: The message body contains the request message as received by the server.</li>
 </ul>
 </dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/201"><code>201 Created</code></a></dt>
 <dd>The request has succeeded and a new resource has been created as a result. This is typically the response sent after <code>POST</code> requests, or some <code>PUT</code> requests.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/202"><code>202 Accepted</code></a></dt>
 <dd>The request has been received but not yet acted upon. It is noncommittal, since there is no way in HTTP to later send an asynchronous response indicating the outcome of the request. It is intended for cases where another process or server handles the request, or for batch processing.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/203"><code>203 Non-Authoritative Information</code></a></dt>
 <dd>This response code means the returned meta-information is not exactly the same as is available from the origin server, but is collected from a local or a third-party copy. This is mostly used for mirrors or backups of another resource. Except for that specific case, the "200 OK" response is preferred to this status.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/204"><code>204 No Content</code></a></dt>
 <dd>There is no content to send for this request, but the headers may be useful. The user-agent may update its cached headers for this resource with the new ones.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/205"><code>205 Reset Content</code></a></dt>
 <dd>Tells the user-agent to reset the document which sent this request.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/206"><code>206 Partial Content</code></a></dt>
 <dd>This response code is used when the <a href="/en-US/docs/Web/HTTP/Headers/Range"><code>Range</code></a> header is sent from the client to request only part of a resource.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/207"><code>207 Multi-Status</code></a> (<a href="/en-US/docs/Glossary/WebDAV">WebDAV</a>)</dt>
 <dd>Conveys information about multiple resources, for situations where multiple status codes might be appropriate.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/208"><code>208 Already Reported</code></a> (<a href="/en-US/docs/Glossary/WebDAV">WebDAV</a>)</dt>
 <dd>Used inside a <code>&lt;dav:propstat&gt;</code> response element to avoid repeatedly enumerating the internal members of multiple bindings to the same collection.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/226"><code>226 IM Used</code></a> (<a href="https://tools.ietf.org/html/rfc3229">HTTP Delta encoding</a>)</dt>
 <dd>The server has fulfilled a <code>GET</code> request for the resource, and the response is a representation of the result of one or more instance-manipulations applied to the current instance.</dd>
</dl></div><h2 id="redirection_messages"><a href="#redirection_messages" title="Permalink to Redirection messages">Redirection messages</a></h2><div><dl>
 <dt><a href="/en-US/docs/Web/HTTP/Status/300"><code>300 Multiple Choice</code></a></dt>
 <dd>The request has more than one possible response. The user-agent or user should choose one of them. (There is no standardized way of choosing one of the responses, but HTML links to the possibilities are recommended so the user can pick.)</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/301"><code>301 Moved Permanently</code></a></dt>
 <dd>The URL of the requested resource has been changed permanently. The new URL is given in the response.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/302"><code>302 Found</code></a></dt>
 <dd>This response code means that the URI of requested resource has been changed <em>temporarily</em>. Further changes in the URI might be made in the future. Therefore, this same URI should be used by the client in future requests.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/303"><code>303 See Other</code></a></dt>
 <dd>The server sent this response to direct the client to get the requested resource at another URI with a GET request.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/304"><code>304 Not Modified</code></a></dt>
 <dd>This is used for caching purposes. It tells the client that the response has not been modified, so the client can continue to use the same cached version of the response.</dd>
 <dt><code>305 Use Proxy</code> <svg class="icon deprecated" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" role="img">
    <title>This deprecated API should no longer be used, but will probably still work.</title>
    <path d="M19.4 24.8a3.6 3.6 0 11-7.2 0 3.6 3.6 0 117.2 0zm9 28.8v-36a3.62 3.62 0 00-3.6-3.6H8.6A3.62 3.62 0 005 17.6v36a3.62 3.62 0 003.6 3.6h16.2a3.62 3.62 0 003.6-3.6zm63.51-8.38A13.16 13.16 0 0195 53.6a11 11 0 01-10.8 10.8H68.62a13.47 13.47 0 001.63 3.6c1.46 2.92 3.15 6.19 3.15 10.8 0 4.33 0 14.4-12.6 14.4a3.54 3.54 0 01-2.53-1.07c-2.42-2.36-3.1-5.85-3.71-9.17s-1.3-6.64-3.49-8.83a75.84 75.84 0 01-5.68-6.75c-2.48-3.26-7.88-10-10-10.12a3.76 3.76 0 01-3.39-3.6V17.6a3.71 3.71 0 013.6-3.6c2-.06 5.34-1.24 8.89-2.47C50.56 9.44 58.16 6.8 66.2 6.8h7.26c5 .06 8.66 1.52 11.08 4.39 2.13 2.53 3.09 6 2.75 10.18a11.47 11.47 0 013 5.29 11.87 11.87 0 010 6.58 11.87 11.87 0 012.42 7.7 15.2 15.2 0 01-.84 4.28z" fill="currentColor"></path>
</svg></dt>
 <dd>Defined in a previous version of the HTTP specification to indicate that a requested response must be accessed by a proxy. It has been deprecated due to security concerns regarding in-band configuration of a proxy.</dd>
 <dt><code>306 unused</code></dt>
 <dd>This response code is no longer used; it is just reserved. It was used in a previous version of the HTTP/1.1 specification.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/307"><code>307 Temporary Redirect</code></a></dt>
 <dd>The server sends this response to direct the client to get the requested resource at another URI with same method that was used in the prior request. This has the same semantics as the <code>302 Found</code> HTTP response code, with the exception that the user agent <em>must not</em> change the HTTP method used: If a <code>POST</code> was used in the first request, a <code>POST</code> must be used in the second request.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/308"><code>308 Permanent Redirect</code></a></dt>
 <dd>This means that the resource is now permanently located at another URI, specified by the <code>Location:</code> HTTP Response header. This has the same semantics as the <code>301 Moved Permanently</code> HTTP response code, with the exception that the user agent <em>must not</em> change the HTTP method used: If a <code>POST</code> was used in the first request, a <code>POST</code> must be used in the second request.</dd>
</dl></div><h2 id="client_error_responses"><a href="#client_error_responses" title="Permalink to Client error responses">Client error responses</a></h2><div><dl>
 <dt><a href="/en-US/docs/Web/HTTP/Status/400"><code>400 Bad Request</code></a></dt>
 <dd>The server could not understand the request due to invalid syntax.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/401"><code>401 Unauthorized</code></a></dt>
 <dd>Although the HTTP standard specifies "unauthorized", semantically this response means "unauthenticated". That is, the client must authenticate itself to get the requested response.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/402"><code>402 Payment Required</code></a> <svg class="icon experimental" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" role="img">
    <title>This is an experimental API that should not be used in production code.</title>
    <path d="M90.72 82.34c4.4 7 1.29 12.66-7 12.66H16.25C8 95 4.88 89.31 9.28 82.34l29.47-46.46V12.5H35A3.75 3.75 0 0135 5h30a3.75 3.75 0 010 7.5h-3.75v23.38zM45.08 39.86L29.14 65h41.72L54.92 39.86l-1.17-1.81V12.5h-7.5v25.55z"></path>
</svg></dt>
 <dd>This response code is reserved for future use. The initial aim for creating this code was using it for digital payment systems, however this status code is used very rarely and no standard convention exists.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/403"><code>403 Forbidden</code></a></dt>
 <dd>The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource. Unlike 401, the client's identity is known to the server.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/404"><code>404 Not Found</code></a></dt>
 <dd>The server can not find the requested resource. In the browser, this means the URL is not recognized. In an API, this can also mean that the endpoint is valid but the resource itself does not exist. Servers may also send this response instead of 403 to hide the existence of a resource from an unauthorized client. This response code is probably the most famous one due to its frequent occurrence on the web.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/405"><code>405 Method Not Allowed</code></a></dt>
 <dd>The request method is known by the server but has been disabled and cannot be used. For example, an API may forbid DELETE-ing a resource. The two mandatory methods, <code>GET</code> and <code>HEAD</code>, must never be disabled and should not return this error code.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/406"><code>406 Not Acceptable</code></a></dt>
 <dd>This response is sent when the web server, after performing <a href="/en-US/docs/HTTP/Content_negotiation#Server-driven_negotiation">server-driven content negotiation</a>, doesn't find any content that conforms to the criteria given by the user agent.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/407"><code>407 Proxy Authentication Required</code></a></dt>
 <dd>This is similar to 401 but authentication is needed to be done by a proxy.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/408"><code>408 Request Timeout</code></a></dt>
 <dd>This response is sent on an idle connection by some servers, even without any previous request by the client. It means that the server would like to shut down this unused connection. This response is used much more since some browsers, like Chrome, Firefox 27+, or IE9, use HTTP pre-connection mechanisms to speed up surfing. Also note that some servers merely shut down the connection without sending this message.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/409"><code>409 Conflict</code></a></dt>
 <dd>This response is sent when a request conflicts with the current state of the server.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/410"><code>410 Gone</code></a></dt>
 <dd>This response is sent when the requested content has been permanently deleted from server, with no forwarding address. Clients are expected to remove their caches and links to the resource. The HTTP specification intends this status code to be used for "limited-time, promotional services". APIs should not feel compelled to indicate resources that have been deleted with this status code.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/411"><code>411 Length Required</code></a></dt>
 <dd>Server rejected the request because the <code>Content-Length</code> header field is not defined and the server requires it.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/412"><code>412 Precondition Failed</code></a></dt>
 <dd>The client has indicated preconditions in its headers which the server does not meet.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/413"><code>413 Payload Too Large</code></a></dt>
 <dd>Request entity is larger than limits defined by server; the server might close the connection or return an <code>Retry-After</code> header field.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/414"><code>414 URI Too Long</code></a></dt>
 <dd>The URI requested by the client is longer than the server is willing to interpret.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/415"><code>415 Unsupported Media Type</code></a></dt>
 <dd>The media format of the requested data is not supported by the server, so the server is rejecting the request.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/416"><code>416 Range Not Satisfiable</code></a></dt>
 <dd>The range specified by the <code>Range</code> header field in the request can't be fulfilled; it's possible that the range is outside the size of the target URI's data.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/417"><code>417 Expectation Failed</code></a></dt>
 <dd>This response code means the expectation indicated by the <code>Expect</code> request header field can't be met by the server.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/418"><code>418 I'm a teapot</code></a></dt>
 <dd>The server refuses the attempt to brew coffee with a teapot.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/421"><code>421 Misdirected Request</code></a></dt>
 <dd>The request was directed at a server that is not able to produce a response. This can be sent by a server that is not configured to produce responses for the combination of scheme and authority that are included in the request URI.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/422"><code>422 Unprocessable Entity</code></a> (<a href="/en-US/docs/Glossary/WebDAV">WebDAV</a>)</dt>
 <dd>The request was well-formed but was unable to be followed due to semantic errors.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/423"><code>423 Locked</code></a> (<a href="/en-US/docs/Glossary/WebDAV">WebDAV</a>)</dt>
 <dd>The resource that is being accessed is locked.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/424"><code>424 Failed Dependency</code></a> (<a href="/en-US/docs/Glossary/WebDAV">WebDAV</a>)</dt>
 <dd>The request failed due to failure of a previous request.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/425"><code>425 Too Early</code></a> <svg class="icon experimental" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" role="img">
    <title>This is an experimental API that should not be used in production code.</title>
    <path d="M90.72 82.34c4.4 7 1.29 12.66-7 12.66H16.25C8 95 4.88 89.31 9.28 82.34l29.47-46.46V12.5H35A3.75 3.75 0 0135 5h30a3.75 3.75 0 010 7.5h-3.75v23.38zM45.08 39.86L29.14 65h41.72L54.92 39.86l-1.17-1.81V12.5h-7.5v25.55z"></path>
</svg></dt>
 <dd>Indicates that the server is unwilling to risk processing a request that might be replayed.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/426"><code>426 Upgrade Required</code></a></dt>
 <dd>The server refuses to perform the request using the current protocol but might be willing to do so after the client upgrades to a different protocol. The server sends an <a href="/en-US/docs/Web/HTTP/Headers/Upgrade"><code>Upgrade</code></a> header in a 426 response to indicate the required protocol(s).</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/428"><code>428 Precondition Required</code></a></dt>
 <dd>The origin server requires the request to be conditional. This response is intended to prevent the 'lost update' problem, where a client GETs a resource's state, modifies it, and PUTs it back to the server, when meanwhile a third party has modified the state on the server, leading to a conflict.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/429"><code>429 Too Many Requests</code></a></dt>
 <dd>The user has sent too many requests in a given amount of time ("rate limiting").</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/431"><code>431 Request Header Fields Too Large</code></a></dt>
 <dd>The server is unwilling to process the request because its header fields are too large. The request may be resubmitted after reducing the size of the request header fields.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/451"><code>451 Unavailable For Legal Reasons</code></a></dt>
 <dd>The user-agent requested a resource that cannot legally be provided, such as a web page censored by a government.</dd>
</dl></div><h2 id="server_error_responses"><a href="#server_error_responses" title="Permalink to Server error responses">Server error responses</a></h2><div><dl>
 <dt><a href="/en-US/docs/Web/HTTP/Status/500"><code>500 Internal Server Error</code></a></dt>
 <dd>The server has encountered a situation it doesn't know how to handle.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/501"><code>501 Not Implemented</code></a></dt>
 <dd>The request method is not supported by the server and cannot be handled. The only methods that servers are required to support (and therefore that must not return this code) are <code>GET</code> and <code>HEAD</code>.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/502"><code>502 Bad Gateway</code></a></dt>
 <dd>This error response means that the server, while working as a gateway to get a response needed to handle the request, got an invalid response.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/503"><code>503 Service Unavailable</code></a></dt>
 <dd>The server is not ready to handle the request. Common causes are a server that is down for maintenance or that is overloaded. Note that together with this response, a user-friendly page explaining the problem should be sent. This responses should be used for temporary conditions and the <code>Retry-After:</code> HTTP header should, if possible, contain the estimated time before the recovery of the service. The webmaster must also take care about the caching-related headers that are sent along with this response, as these temporary condition responses should usually not be cached.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/504"><code>504 Gateway Timeout</code></a></dt>
 <dd>This error response is given when the server is acting as a gateway and cannot get a response in time.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/505"><code>505 HTTP Version Not Supported</code></a></dt>
 <dd>The HTTP version used in the request is not supported by the server.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/506"><code>506 Variant Also Negotiates</code></a></dt>
 <dd>The server has an internal configuration error: the chosen variant resource is configured to engage in transparent content negotiation itself, and is therefore not a proper end point in the negotiation process.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/507"><code>507 Insufficient Storage</code></a> (<a href="/en-US/docs/Glossary/WebDAV">WebDAV</a>)</dt>
 <dd>The method could not be performed on the resource because the server is unable to store the representation needed to successfully complete the request.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/508"><code>508 Loop Detected</code></a> (<a href="/en-US/docs/Glossary/WebDAV">WebDAV</a>)</dt>
 <dd>The server detected an infinite loop while processing the request.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/510"><code>510 Not Extended</code></a></dt>
 <dd>Further extensions to the request are required for the server to fulfil it.</dd>
 <dt><a href="/en-US/docs/Web/HTTP/Status/511"><code>511 Network Authentication Required</code></a></dt>
 <dd>The 511 status code indicates that the client needs to authenticate to gain network access.</dd>
</div></article>
