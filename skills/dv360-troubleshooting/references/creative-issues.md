# Playbook: creative disapproved or not serving

**Symptom.** A creative is disapproved or rejected, or a line item with an assigned creative is not serving and the creative status is the suspect.

A creative serves only when its status is **Approved** or **Servable**. **Pending** (still under review or still a draft) and **Rejected** (an issue must be fixed) do not serve. Approved creatives remain subject to recurring reviews, so a previously running creative can flip to Rejected later.

## Creative statuses

- **Pending.** Under review or still a draft. Cannot serve yet.
- **Servable.** Approved for serving while additional review continues. Can serve now.
- **Approved.** Fully approved. Can serve. Still subject to periodic re-review.
- **Rejected.** A problem must be fixed before it can serve.

## Ordered checks

1. **Find the rejected creatives.** The Intelligence panel flags rejected creatives on the campaign. Open the list and select the creative to review.
2. **Read the feedback.** Open the creative and read the Creative status feedback, which states the rejection reason. Do not guess; the feedback names the policy or technical cause.
3. **Classify the cause.** Rejections fall into a few classes: technical (wrong dimensions, unsupported or broken format, missing or inactive video assets in a VAST creative, unfetchable third-party tags), content policy (prohibited or restricted content), and landing-page (uncrawlable destination, malware, or non-SSL page).
4. **Fix the cause.**
   - Technical: correct the dimensions, format, or assets, or fix the third-party tag so it fetches and renders.
   - Content policy: edit the creative to comply.
   - Landing page: use a compliant page, or fix the destination (crawlability, security, SSL) with the site owner.
5. **Resubmit.** After fixing, resubmit for approval. Resubmission restarts the review process and returns the creative to pending, so it cannot serve again until it reaches servable or approved.
6. **Appeal a policy error.** If you believe the rejection or a policy restriction is wrong, dispute the decision within the platform for review.

## Fix

Read the feedback, fix the named cause, resubmit, and expect a pending period before serving resumes. If a creative was serving and stopped, check for a recurring-review flip to Rejected and treat it the same way.

## Cross-links

- Creative compatibility with line item type as a no-delivery cause: `no-delivery.md`.
- Brand-safety constraints that interact with creative eligibility: `dv360-frequency-and-brand-safety`.
