
public class Document {
	private String title;
	private String url;
	private String description;

	public Document(String t, String u, String d) {
		title=t;
		url=u;
		description=d;
	}

	public String getTitle() {
		return title;
	}
	public void setTitle(String t) {
		title=t;
	}

	public String getUrl() {
		return url;
	}
	public void setUrl(String u) {
		url=u;
	}

	public String getDescription() {
		return description;
	}
	public void setDescription(String d) {
		description=d;
	}
}