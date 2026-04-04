# Meta Account Setup Checklist

---

## Step-by-Step Setup

### 1. Create Meta Business Manager (Day 1)
- [ ] Go to business.facebook.com
- [ ] Create a new Business Manager account with the LLC's legal name
- [ ] Add your personal Facebook account as admin
- **Time:** 15 minutes
- **Gotcha:** Use the business legal name, not a personal name. This matters for verification.

### 2. Business Verification (Days 1-5)
- [ ] Go to Security Center in Business Manager
- [ ] Submit business verification documents:
  - LLC Certificate of Formation (from Delaware)
  - EIN confirmation letter (from IRS)
  - Utility bill or bank statement with business address (registered agent address works)
- [ ] Wait for Meta review
- **Time:** 1-5 business days (sometimes instant, sometimes a week)
- **Gotcha:** This is the #1 bottleneck. Without verification, you're locked to low spending limits and can't access advanced features. **Start this ASAP.**

### 3. Create Ad Account (Day 1)
- [ ] In Business Manager → Ad Accounts → Create
- [ ] Set currency (USD) and time zone (Eastern)
- [ ] Set the account spending limit high ($50K+) or remove it
- **Time:** 5 minutes
- **Gotcha:** Currency and time zone CANNOT be changed after creation.

### 4. Install Meta Pixel on Shopify (Day 1)
- [ ] In Shopify admin → Settings → Apps → Facebook & Instagram
- [ ] Connect your Meta Business Manager
- [ ] Install the pixel
- [ ] Verify pixel fires: ViewContent, AddToCart, InitiateCheckout, Purchase
- [ ] Set up Conversions API (CAPI) for server-side tracking (Shopify does this automatically through the integration)
- **Time:** 30 minutes
- **Gotcha:** iOS 14.5+ privacy changes mean pixel-only tracking misses 30-40% of conversions. CAPI is essential.

### 5. Add Payment Method (Day 1)
- [ ] Add a credit card with high limit ($10K+ recommended)
- [ ] Consider adding a backup payment method
- **Time:** 5 minutes
- **Gotcha:** If your card declines (hits limit), Meta pauses all ads immediately. Have backup payment ready.

### 6. Set Up Domain Verification (Day 1)
- [ ] In Business Manager → Brand Safety → Domains
- [ ] Add your Shopify domain
- [ ] Verify via DNS TXT record or meta tag
- [ ] Configure Aggregated Event Measurement (AEM) — prioritize Purchase as #1 event
- **Time:** 15-30 minutes
- **Gotcha:** Without domain verification, your event tracking is limited to 8 events and you can't optimize for purchases effectively.

### 7. Create Facebook Page (Day 1)
- [ ] Create a business Page for your brand
- [ ] Add profile photo (logo) and cover image
- [ ] Add basic info (website, description)
- **Time:** 15 minutes

### 8. Create Instagram Business Account (Day 1)
- [ ] Create or convert to a business account
- [ ] Link to Facebook Page
- [ ] Post 3-5 initial content pieces (shirt mockups, behind-the-scenes)
- **Time:** 30 minutes
- **Gotcha:** Ads from accounts with zero posts look spammy. Have at least 3-5 posts before running ads.

### 9. Request Spending Limit Increase (Week 2+)
- [ ] After business verification, contact Meta support
- [ ] Request higher daily spending limits
- [ ] Provide revenue projections and business context
- **Time:** 1-3 business days per request
- **Gotcha:** New accounts are often capped at $50-250/day initially. Budget ramp requires patience.

### 10. Ad Policy Pre-Check (Before Launch)
- [ ] Review Meta's ad policies for apparel/merch
- [ ] Ensure no IP-infringing content in ad creatives
- [ ] Test-submit 2-3 ads to check for policy rejections before the main launch
- **Time:** 1-2 days for review
- **Gotcha:** Meta's automated review can reject ads for unexpected reasons. Test early.

---

## Timeline Summary

| Task | When | Duration | Blocker? |
|---|---|---|---|
| Create Business Manager + Ad Account | Day 1 | 30 min | No |
| Submit Business Verification | Day 1 | 1-5 days to approve | **YES — Critical path** |
| Create Page + Instagram | Day 1 | 45 min | No |
| Install Pixel + CAPI | Day 1 (after Shopify is live) | 30 min | Needs Shopify store |
| Domain Verification | Day 1 | 15 min | Needs domain |
| Payment Method | Day 1 | 5 min | No |
| Test Ads Submitted | Day 3-5 | 1-2 days for review | Needs verification |
| Spending Limit Ramp | Weeks 2-6 | Ongoing | Needs trust building |

**Total calendar time to full readiness: 5-10 business days**
**Recommendation: Start setup by May 1, 2026 at the latest. Earlier is better — run small test campaigns through May/June to build account trust before the real launch.**

---

## Common Hangups

1. **Business verification rejected** — Wrong documents, name mismatch between LLC and BM. Fix: Ensure exact legal name match.
2. **Ad account disabled** — Triggered by policy violations or suspicious activity. Fix: Appeal through Business Support. Can take 1-14 days.
3. **Pixel not firing** — Shopify integration issue. Fix: Use Meta Pixel Helper Chrome extension to debug.
4. **Payment declined** — Card limit hit. Fix: Use a business credit card with $20K+ limit.
5. **Low spending limits** — New account trust issue. Fix: Start with small spend, build gradually, request increases through support.

---

## Sources

- [How to Use Meta Ads Manager 2026 — Shopify](https://www.shopify.com/blog/facebook-ads-manager)
- [About Daily Spending Limits — Meta Business Help](https://www.facebook.com/business/help/563129151097553)
- [Meta Ads 10 Essential Rules for 2026 — Div Digital](https://www.div.digital/meta-ads-10-essential-rules-for-2026/)
